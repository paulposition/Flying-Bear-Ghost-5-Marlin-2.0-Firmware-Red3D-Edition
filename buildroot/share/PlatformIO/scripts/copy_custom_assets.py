Import("env")
import os

custom_bmp_toolpath = os.path.join(env.Dictionary("PROJECT_DIR"), "custom_bmp") + "/"
custom_bmp_path = os.path.join(env.Dictionary("PROJECT_DIR"), "custom_bmp", "images") + "/"
assets_path = os.path.join(env.Dictionary("PROJECT_BUILD_DIR"), env.Dictionary("PIOENV"), "assets")

def convert_assets():
	print("*** Converting Assets *** ")
	if os.path.exists(assets_path) == True and os.path.isdir(assets_path) == False:
		os.unlink(assets_path)
	if os.path.exists(assets_path) == False:
		os.mkdir(assets_path)
	for filename in os.listdir(custom_bmp_path):
		if ".png" in filename:			
			img_name=os.path.splitext(filename)[0]
			command = 'php '+custom_bmp_toolpath+'/_img_conv_core.php "name='+img_name+'&img='+custom_bmp_path+"/"+filename+'&cf=true_color&format=bin_565&out='+assets_path+'/"'
			print("-> " + img_name )
			os.system(command)

convert_assets()

