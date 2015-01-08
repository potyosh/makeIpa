import sys
import subprocess
import config as conf
from svnmods import Svnmods

#Functions
def execCommand(argCmd):
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout_data, stderr__data = p.communicate()
	return stdout_data

#Main Program

#Directory Clean
cmd = "rm -rf "+conf.PROJECT_ROOT+"/"+conf.APP_DIR
print execCommand(cmd)

cmd = "rm -rf "+conf.PROJECT_ROOT+"/"+conf.IPA_DIR
print execCommand(cmd)

cmd = "mkdir "+conf.PROJECT_ROOT+"/"+conf.APP_DIR
print execCommand(cmd)

cmd = "mkdir "+conf.PROJECT_ROOT+"/"+conf.IPA_DIR
print execCommand(cmd)

cmd = "mkdir "+conf.PROJECT_ROOT+"/"+conf.APP_DIR+"/"+conf.APP_DIR
print execCommand(cmd)

cmd = "mkdir "+conf.PROJECT_ROOT+"/"+conf.IPA_DIR+"/"+conf.IPA_DIR
print execCommand(cmd)

cmd = "mkdir "+conf.PROJECT_ROOT+"/"+conf.APP_DIR+"/"+conf.APP_DIR
print execCommand(cmd)

cmd = "mkdir "+conf.PROJECT_ROOT+"/"+conf.IPA_DIR+"/"+conf.IPA_DIR
print execCommand(cmd)

#Project Clean
cmd = "xcodebuild clean -project "+conf.PROJECT
print execCommand(cmd)

#Project Build
cmd = "xcodebuild -project "+conf.PROJECT+" -sdk "+conf.SDK+" -configuration "+conf.CONFIGURATION+" -target "+conf.TARGET_NAME+" install DSTROOT="+conf.APP_DIR+"/"+conf.APP_DIR+" "+conf.CODE_SIGN_IDENTITY
print execCommand(cmd)

#Generate ipa
svnModule = Svnmods(conf.SVN_REPOSITORY)
svnRevNum = svnModule.getSvnRevNum()
cmd = "xcrun -sdk "+conf.SDK+" PackageApplication "+conf.PROJECT_ROOT+"/"+"/"+conf.APP_DIR+"/"+"Applications"+"/"+conf.TARGET_NAME+".app"+" -o "+conf.PROJECT_ROOT+"/"+conf.IPA_DIR+"/"+"/"+conf.PRODUCT_NAME+str(svnRevNum)+".ipa"+" -embed "+conf.PROVISIONING
print execCommand(cmd)

