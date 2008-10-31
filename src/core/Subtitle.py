
import os


class SubtitleSrt(object):
    
    def __init__(self, outputPath):
        self.__outputPath = outputPath
        self.__index = 0
        self.__curTime = 0.0
        
    def __FormatTime(self, totalSecs):
        minutes = int(totalSecs) / 60
        hours = int(minutes) / 60
        seconds = int(totalSecs) % 60
        frac = int((totalSecs - int(totalSecs)) * 1000)
        return "%02d:%02d:%02d,%03d" % (hours, minutes, seconds, frac)
    
    def __ProcessPic(self, pic):
        start = self.__FormatTime(self.__curTime + 0.5)
        end   = self.__FormatTime(self.__curTime + pic.GetDuration() - 0.5)
        
        result = "%(idx)d\n" \
                 "%(start)s --> %(end)s\n" \
                 "%(text)s\n" \
                 "\n" % {'idx': self.__index,
                         'start': start,
                         'end': end,
                         'text': pic.GetComment().strip()}
                 
        return result
        
    
    def Start(self, pics):
        fd = open(os.path.join(self.__outputPath, "output.srt"), 'w')
        for pic in pics:
            self.__index += 1
            
            data = self.__ProcessPic(pic)
            fd.write(data)
            
            self.__curTime += pic.GetDuration()
            
        fd.close()
        
        
def test():
    from core.Picture import Picture
    p1 = Picture(None)
    p1.SetComment("this is my first picture")
    p1.SetDuration(7)

    p2 = Picture(None)
    p2.SetComment("this is my second picture")
    p2.SetDuration(12)
    
    p3 = Picture(None)
    p3.SetComment("this is my third picture")
    p3.SetDuration(2)
    
    s = SubtitleSrt(".")
    s.Start([p1, p2, p3])
    
if __name__ == "__main__":
    test()
