Set Path=%Path%;%~dp0..\python276_bin;;C:\Program Files\TortoiseSVN\bin
set DEPOT_TOOLS_WIN_TOOLCHAIN=1
set GYP_MSVS_VERSION=2013e
set GYP_GENERATORS=msvs-ninja,ninja
set GYP_DEFINES=component=shared_library buildtype=Official

call ninja -C out/Release  gen_demo_resource
call ninja -C out/Debug    gen_demo_resource

call All.sln