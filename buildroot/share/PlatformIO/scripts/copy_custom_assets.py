Import("env")
import os
import shutil

custom_graphics_toolpath = os.path.join(env.Dictionary("PROJECT_DIR"), "custom_graphics") + "/"
custom_graphics_path = os.path.join(env.Dictionary("PROJECT_DIR"), "custom_graphics", "images") + "/"
assets_path = os.path.join(env.Dictionary("PROJECT_BUILD_DIR"), env.Dictionary("PIOENV"), "assets")

def convert_assets():
	print("*** Converting Assets *** ")
	shutil.rmtree(assets_path, ignore_errors=True)
	if os.path.exists(assets_path) == False:
		os.mkdir(assets_path)
	for filename in os.listdir(custom_graphics_path):
		if ".png" in filename:			
			img_name=os.path.splitext(filename)[0]
			command = 'php '+custom_graphics_toolpath+'/_img_conv_core.php "name='+img_name+'&img='+custom_graphics_path+"/"+filename+'&cf=true_color&format=bin_565&out='+assets_path+'/"'
			print("-> " + img_name )
			os.system(command)

convert_assets()

