
{  
  'includes': [
    '../../../build/win_precompile.gypi',
    'imgdecoder-gdip.gypi',
  ],
  'targets': [
    {
      'target_name': 'imgdecoder-gdip',
      'type': '<(component)',
      'includes': [ '../../build/common.gypi', ],  
      'dependencies': [
      		'<(app_root)/third-part/zlib/zlib.gyp:*',
      		'<(app_root)/third-part/png/png.gyp:*',
      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
