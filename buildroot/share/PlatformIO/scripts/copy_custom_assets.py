Import("env")
import os
import shutil

custom_graphics_toolpath = os.path.join(env.Dictionary("PROJECT_DIR"), "custom_graphics") + "/"
custom_graphics_path = os.path.join(env.Dictionary("PROJECT_DIR"), "custom_graphics", "images") + "/"
custom_fonts_path = os.path.join(env.Dictionary("PROJECT_DIR"), "custom_graphics", "fonts") + "/"
assets_path = os.path.join(env.Dictionary("PROJECT_BUILD_DIR"), env.Dictionary("PIOENV"), "assets")

def convert_assets():
	print("*** Converting Assets *** ")
	for filename in os.listdir(custom_graphics_path):
		if ".png" in filename:			
			img_name=os.path.splitext(filename)[0]
			command = 'php '+custom_graphics_toolpath+'/_img_conv_core.php "name='+img_name+'&img='+custom_graphics_path+"/"+filename+'&cf=true_color&format=bin_565&out='+assets_path+'/"'
			print("-> " + filename )
			os.system(command)

def copy_fonts():
	print("*** Copying Fonts *** ")
	for filename in os.listdir(custom_fonts_path):
		if ".bin" in filename:	
			print("-> " + filename )
			shutil.copy(os.path.join(custom_fonts_path, filename), assets_path)	



shutil.rmtree(assets_path, ignore_errors=True)
if os.path.exists(assets_path) == False:
	os.mkdir(assets_path)

convert_assets()
copy_fonts()

