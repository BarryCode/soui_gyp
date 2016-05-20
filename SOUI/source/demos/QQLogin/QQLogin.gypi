
{
  'target_defaults': {
   
    'sources': [
      #include files			
			'GroupChatFrame.h',
			'MainDlg.h',
			'resource.h',
			'stdafx.h',
			'utils.h',
			'extend.ctrls/ExtendCtrls.h',
			'extend.ctrls/SButtonEx.h',
			'extend.ctrls/SImageEx.h',
			'extend.ctrls/SImagePlayer.h',
			'extend.ctrls/SSplitBar.h',
			'extend.ctrls/SText.h',
			'extend.skins/ExtendSkins.h',
			'extend.skins/SAniImgFrame.h',
			'extend.skins/SSkinMutiFrameImg.h',
			'extend.ctrls/imre/ImgProvider.h',
			'extend.ctrls/imre/IRichEditObjHost.h',
			'extend.ctrls/imre/RichEditObj.h',
			'extend.ctrls/imre/RichEditObjFactory.h',
			'extend.ctrls/imre/RichEditOleBase.h',
			'extend.ctrls/imre/RichEditOleCallback.h',
			'extend.ctrls/imre/RichEditOleCtrls.h',
			'extend.ctrls/imre/SImRichEdit.h',
			'extend.ctrls/imre/TOM2.h',
			'../../controls.extend/SChromeTabCtrl.h',
			'../../controls.extend/SImageMaskWnd.h',
			'../../controls.extend/STurn3DView.h',
			'../../controls.extend/image3d/3dlib.h',
			'../../controls.extend/image3d/3dmatrix.h',
			'../../controls.extend/image3d/3dTransform.h',
			'../../controls.extend/FileHelper.h',
			'../../controls.extend/slistboxex.h',
			
			'GroupChatFrame.cpp',
			'MainDlg.cpp',
			'QQLogin.cpp',
			'utils.cpp',
			'extend.ctrls/ExtendCtrls.cpp',
			'extend.ctrls/SButtonEx.cpp',
			'extend.ctrls/SImageEx.cpp',
			'extend.ctrls/SImagePlayer.cpp',
			'extend.ctrls/SplitBar.cpp',
			'extend.ctrls/SText.cpp',
			'extend.skins/ExtendSkins.cpp',
			'extend.skins/SSkinMutiFrameImg.cpp',
			'extend.ctrls/imre/ImgProvider.cpp',
			'extend.ctrls/imre/RichEditObj.cpp',
			'extend.ctrls/imre/RichEditObjFactory.cpp',
			'extend.ctrls/imre/RichEditOleBase.cpp',
			'extend.ctrls/imre/RichEditOleCallback.cpp',
			'extend.ctrls/imre/RichEditOleCtrls.cpp',
			'extend.ctrls/imre/SImRichedit.cpp',
			'../../controls.extend/SChromeTabCtrl.cpp',
			'../../controls.extend/SImageMaskWnd.cpp',
			'../../controls.extend/STurn3DView.cpp',
			'../../controls.extend/image3d/3dlib.cpp',
			'../../controls.extend/image3d/3dmatrix.cpp',
			'../../controls.extend/image3d/3dtransform.cpp',
			'../../controls.extend/slistboxex.cpp',

		  'QQLogin.rc',
    ],
    'include_dirs': [ 
      '.',
      '../../config',
			'../../utilities/include',
			'../../soui/include',
			'../../components',
    ],
    'direct_dependent_settings': {
        'include_dirs': [
          '.',
        ],
    },
    'configurations': {
	      'Debug': {
	        # Specify third party library directory
          'msvs_settings': {
            'VCLinkerTool': {
              "AdditionalLibraryDirectories": [
			          #'../3rd/detours/lib',  
              ],
              'SubSystem': '2', #/SUBSYSTEM:WINDOWS
            },
          },
	      },
	      'Release': {
	        # Specify third party library directory
          'msvs_settings': {
            'VCLinkerTool': {
              "AdditionalLibraryDirectories": [
			          #'../3rd/detours/lib', 
              ],
              'SubSystem': '2', #/SUBSYSTEM:WINDOWS
            },
          },
	      }
    }, # configurations
  },
}
