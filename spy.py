#-*- coding: utf8 -*-
import os
import sys

class SpyFolders():
    
    def get_files_list_from_dir(self,dir,ext = None):
        allfiles = []
        needExtFilter = (ext != None)
        for root,dirs,files in os.walk(dir):
            for filespath in files:
                filespath = os.path.join(root,filespath)
                extension = os.path.splitext(filespath)[1][1:]
                if needExtFilter and extension in ext:
                    allfiles.append(filespath)
                elif not needExtFilter:
                    allfiles.append(filespath)
        return allfiles

    def main(self):
        os.chdir("d:"+os.sep+"work")
        files = self.get_files_list_from_dir(os.getcwd())
        for item in files:
            print (item)
        pass

    def get_files(self):
        os.chdir("d:"+os.sep+"work")
        files = self.get_files_list_from_dir(os.getcwd())
        return files
        

if __name__ == "__main__":
    runner = SpyFolders()
    runner.main()
    #runner.debugFunction()

    sys.exit()
