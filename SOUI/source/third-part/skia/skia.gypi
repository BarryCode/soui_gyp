
{
  'target_defaults': {
    'defines': [
      'SK_IGNORE_ETC1_SUPPORT',
      'SK_CPU_SSE_LEVEL=31',
    ],
    'sources': [
        #include files	
        'src/fonts/SkFontMgr_indirect.cpp',
				'src/fonts/SkGScalerContext.cpp',
				'src/fonts/SkGScalerContext.h',
				'src/fonts/SkRemotableFontMgr.cpp',
				'src/fonts/SkTestScalerContext.cpp',
				'src/fonts/SkTestScalerContext.h',
				'src/utils/SkBase64.cpp',
				'src/utils/SkBase64.h',
				'src/utils/SkBitmapHasher.cpp',
				'src/utils/SkBitmapHasher.h',
				'src/utils/SkBitSet.cpp',
				'src/utils/SkBitSet.h',
				'src/utils/SkBoundaryPatch.cpp',
				'src/utils/SkCamera.cpp',
				'src/utils/SkCanvasStack.cpp',
				'src/utils/SkCanvasStack.h',
				'src/utils/SkCanvasStateUtils.cpp',
				'src/utils/SkCondVar.cpp',
				'src/utils/SkCondVar.h',
				'src/utils/SkCubicInterval.cpp',
				'src/utils/SkCullPoints.cpp',
				'src/utils/SkDashPath.cpp',
				'src/utils/SkDashPathPriv.h',
				'src/utils/SkDumpCanvas.cpp',
				'src/utils/SkEventTracer.cpp',
				'src/utils/SkFloatUtils.h',
				'src/utils/SkFrontBufferedStream.cpp',
				'src/utils/SkGatherPixelRefsAndRects.cpp',
				'src/utils/SkGatherPixelRefsAndRects.h',
				'src/utils/SkInterpolator.cpp',
				'src/utils/SkLayer.cpp',
				'src/utils/SkMatrix22.cpp',
				'src/utils/SkMatrix22.h',
				'src/utils/SkMatrix44.cpp',
				'src/utils/SkMD5.cpp',
				'src/utils/SkMD5.h',
				'src/utils/SkMeshUtils.cpp',
				'src/utils/SkNinePatch.cpp',
				'src/utils/SkNullCanvas.cpp',
				'src/utils/SkNWayCanvas.cpp',
				'src/utils/SkOSFile.cpp',
				'src/utils/SkParse.cpp',
				'src/utils/SkParseColor.cpp',
				'src/utils/SkParsePath.cpp',
				'src/utils/SkPatchGrid.cpp',
				'src/utils/SkPatchGrid.h',
				'src/utils/SkPatchUtils.cpp',
				'src/utils/SkPatchUtils.h',
				'src/utils/SkPathUtils.cpp',
				'src/utils/SkPictureUtils.cpp',
				'src/utils/SkProxyCanvas.cpp',
				'src/utils/SkRTConf.cpp',
				'src/utils/SkRunnable.h',
				'src/utils/SkSHA1.cpp',
				'src/utils/SkSHA1.h',
				'src/utils/SkTextureCompressor.cpp',
				'src/utils/SkTextureCompressor.h',
				'src/utils/SkTextureCompressor_ASTC.cpp',
				'src/utils/SkTextureCompressor_ASTC.h',
				'src/utils/SkTextureCompressor_Blitter.h',
				'src/utils/SkTextureCompressor_LATC.cpp',
				'src/utils/SkTextureCompressor_LATC.h',
				'src/utils/SkTextureCompressor_R11EAC.cpp',
				'src/utils/SkTextureCompressor_R11EAC.h',
				'src/utils/SkTFitsIn.h',
				#'src/utils/SkThreadPool.h',
				'src/utils/SkThreadUtils.h',
				'src/utils/SkThreadUtils_win.cpp',
				'src/utils/SkThreadUtils_win.h',
				'src/utils/SkTLogic.h',
				'src/utils/win/SkAutoCoInitialize.cpp',
				'src/utils/win/SkHRESULT.cpp',
				'src/utils/win/SkIStream.cpp',
				'src/utils/win/SkWGL_win.cpp',
				'src/core/SkAAClip.cpp',
				'src/core/SkAdvancedTypefaceMetrics.cpp',
				'src/core/SkAlphaRuns.cpp',
				'src/core/SkAnnotation.cpp',
				'src/core/SkAntiRun.h',
				'src/core/SkBBHFactory.cpp',
				'src/core/SkBBoxHierarchy.h',
				'src/core/SkBBoxHierarchyRecord.cpp',
				'src/core/SkBBoxHierarchyRecord.h',
				'src/core/SkBBoxRecord.cpp',
				'src/core/SkBBoxRecord.h',
				'src/core/SkBitmap.cpp',
				'src/core/SkBitmap_scroll.cpp',
				'src/core/SkBitmapCache.cpp',
				'src/core/SkBitmapDevice.cpp',
				'src/core/SkBitmapFilter.cpp',
				'src/core/SkBitmapFilter.h',
				'src/core/SkBitmapHeap.cpp',
				'src/core/SkBitmapHeap.h',
				'src/core/SkBitmapProcShader.cpp',
				'src/core/SkBitmapProcShader.h',
				'src/core/SkBitmapProcState.cpp',
				'src/core/SkBitmapProcState.h',
				'src/core/SkBitmapProcState_matrix.h',
				'src/core/SkBitmapProcState_matrixProcs.cpp',
				'src/core/SkBitmapProcState_sample.h',
				'src/core/SkBitmapScaler.cpp',
				'src/core/SkBitmapScaler.h',
				'src/core/SkBlitBWMaskTemplate.h',
				'src/core/SkBlitMask_D32.cpp',
				'src/core/SkBlitRow_D16.cpp',
				'src/core/SkBlitRow_D32.cpp',
				'src/core/SkBlitter.cpp',
				'src/core/SkBlitter.h',
				'src/core/SkBlitter_A8.cpp',
				'src/core/SkBlitter_ARGB32.cpp',
				'src/core/SkBlitter_RGB16.cpp',
				'src/core/SkBlitter_Sprite.cpp',
				'src/core/SkBuffer.cpp',
				'src/core/SkCanvas.cpp',
				'src/core/SkChunkAlloc.cpp',
				'src/core/SkClipStack.cpp',
				'src/core/SkColor.cpp',
				'src/core/SkColorFilter.cpp',
				'src/core/SkColorTable.cpp',
				'src/core/SkComposeShader.cpp',
				'src/core/SkConfig8888.cpp',
				'src/core/SkConfig8888.h',
				'src/core/SkConvolver.cpp',
				'src/core/SkConvolver.h',
				'src/core/SkCoreBlitters.h',
				'src/core/SkCubicClipper.cpp',
				'src/core/SkCubicClipper.h',
				'src/core/SkData.cpp',
				'src/core/SkDataTable.cpp',
				'src/core/SkDebug.cpp',
				'src/core/SkDeque.cpp',
				'src/core/SkDevice.cpp',
				'src/core/SkDeviceLooper.cpp',
				'src/core/SkDeviceProfile.cpp',
				'src/core/SkDistanceFieldGen.cpp',
				'src/core/SkDistanceFieldGen.h',
				'src/core/SkDither.cpp',
				'src/core/SkDraw.cpp',
				'src/core/SkDrawLooper.cpp',
				'src/core/SkDrawProcs.h',
				'src/core/SkEdge.cpp',
				'src/core/SkEdge.h',
				'src/core/SkEdgeBuilder.cpp',
				'src/core/SkEdgeClipper.cpp',
				'src/core/SkError.cpp',
				'src/core/SkErrorInternals.h',
				'src/core/SkFilterProc.cpp',
				'src/core/SkFilterProc.h',
				'src/core/SkFilterShader.cpp',
				'src/core/SkFlattenable.cpp',
				'src/core/SkFlattenableSerialization.cpp',
				'src/core/SkFloat.cpp',
				'src/core/SkFloat.h',
				'src/core/SkFloatBits.cpp',
				'src/core/SkFont.cpp',
				'src/core/SkFontDescriptor.cpp',
				'src/core/SkFontDescriptor.h',
				'src/core/SkFontHost.cpp',
				'src/core/SkFontStream.cpp',
				'src/core/SkFontStream.h',
				'src/core/SkGeometry.cpp',
				'src/core/SkGlyphCache.cpp',
				'src/core/SkGlyphCache.h',
				'src/core/SkGlyphCache_Globals.h',
				'src/core/SkGraphics.cpp',
				'src/core/SkImageFilter.cpp',
				'src/core/SkImageGenerator.cpp',
				'src/core/SkImageInfo.cpp',
				'src/core/SkInstCnt.cpp',
				'src/core/SkLineClipper.cpp',
				'src/core/SkLocalMatrixShader.cpp',
				'src/core/SkMallocPixelRef.cpp',
				'src/core/SkMask.cpp',
				'src/core/SkMaskFilter.cpp',
				'src/core/SkMaskGamma.cpp',
				'src/core/SkMaskGamma.h',
				'src/core/SkMath.cpp',
				'src/core/SkMatrix.cpp',
				'src/core/SkMessageBus.h',
				'src/core/SkMetaData.cpp',
				'src/core/SkMipMap.cpp',
				'src/core/SkMultiPictureDraw.cpp',
				'src/core/SkPackBits.cpp',
				'src/core/SkPaint.cpp',
				'src/core/SkPaintPriv.cpp',
				'src/core/SkPaintPriv.h',
				'src/core/SkPath.cpp',
				'src/core/SkPathEffect.cpp',
				'src/core/SkPathHeap.cpp',
				'src/core/SkPathHeap.h',
				'src/core/SkPathMeasure.cpp',
				'src/core/SkPathRef.cpp',
				'src/core/SkPicture.cpp',
				'src/core/SkPictureContentInfo.cpp',
				'src/core/SkPictureContentInfo.h',
				'src/core/SkPictureData.cpp',
				'src/core/SkPictureData.h',
				'src/core/SkPictureFlat.cpp',
				'src/core/SkPictureFlat.h',
				'src/core/SkPicturePlayback.cpp',
				'src/core/SkPicturePlayback.h',
				'src/core/SkPictureRecord.cpp',
				'src/core/SkPictureRecord.h',
				'src/core/SkPictureRecorder.cpp',
				'src/core/SkPictureShader.cpp',
				'src/core/SkPictureShader.h',
				'src/core/SkPictureStateTree.cpp',
				'src/core/SkPictureStateTree.h',
				'src/core/SkPixelRef.cpp',
				'src/core/SkPoint.cpp',
				'src/core/SkProcSpriteBlitter.cpp',
				'src/core/SkPtrRecorder.cpp',
				'src/core/SkQuadClipper.cpp',
				'src/core/SkQuadClipper.h',
				'src/core/SkRasterClip.cpp',
				'src/core/SkRasterizer.cpp',
				'src/core/SkReadBuffer.cpp',
				'src/core/SkReadBuffer.h',
				'src/core/SkReader32.h',
				'src/core/SkRecordDraw.cpp',
				'src/core/SkRecorder.cpp',
				'src/core/SkRecording.cpp',
				'src/core/SkRecordOpts.cpp',
				'src/core/SkRect.cpp',
				'src/core/SkRefDict.cpp',
				'src/core/SkRegion.cpp',
				'src/core/SkRegion_path.cpp',
				'src/core/SkRegionPriv.h',
				'src/core/SkRRect.cpp',
				'src/core/SkRTree.cpp',
				'src/core/SkRTree.h',
				'src/core/SkScalar.cpp',
				'src/core/SkScalerContext.cpp',
				'src/core/SkScalerContext.h',
				'src/core/SkScan.cpp',
				'src/core/SkScan.h',
				'src/core/SkScan_Antihair.cpp',
				'src/core/SkScan_AntiPath.cpp',
				'src/core/SkScan_Hairline.cpp',
				'src/core/SkScan_Path.cpp',
				'src/core/SkScanPriv.h',
				'src/core/SkShader.cpp',
				'src/core/SkSinTable.h',
				'src/core/SkSpriteBlitter.h',
				'src/core/SkSpriteBlitter_ARGB32.cpp',
				'src/core/SkSpriteBlitter_RGB16.cpp',
				'src/core/SkSpriteBlitterTemplate.h',
				'src/core/SkStream.cpp',
				'src/core/SkStreamPriv.h',
				'src/core/SkString.cpp',
				'src/core/SkStringUtils.cpp',
				'src/core/SkStroke.cpp',
				'src/core/SkStroke.h',
				'src/core/SkStrokeRec.cpp',
				'src/core/SkStrokerPriv.cpp',
				'src/core/SkStrokerPriv.h',
				'src/core/SkTextBlob.cpp',
				'src/core/SkTextFormatParams.h',
				'src/core/SkTextMapStateProc.h',
				'src/core/SkTileGrid.cpp',
				'src/core/SkTileGrid.h',
				'src/core/SkTLList.h',
				'src/core/SkTLS.cpp',
				'src/core/SkTraceEvent.h',
				'src/core/SkTSearch.cpp',
				'src/core/SkTSort.h',
				'src/core/SkTypeface.cpp',
				'src/core/SkTypefaceCache.cpp',
				'src/core/SkTypefaceCache.h',
				'src/core/SkUnPreMultiply.cpp',
				'src/core/SkUtils.cpp',
				'src/core/SkValidatingReadBuffer.cpp',
				'src/core/SkVertState.cpp',
				'src/core/SkWriteBuffer.cpp',
				'src/core/SkWriter32.cpp',
				'src/core/SkXfermode.cpp',
				'src/core/SkResourceCache.cpp',
				'src/core/SkResourceCache.h',
				
				'src/doc\SkDocument.cpp',
				'src/image\SkImage.cpp',
				'src/image\SkImage_Raster.cpp',
				'src/image\SkImagePriv.cpp',
				'src/image\SkSurface.cpp',
				'src/image\SkSurface_Base.h',
				'src/image\SkSurface_Raster.cpp',
				'src/lazy\SkCachingPixelRef.cpp',
				'src/lazy\SkCachingPixelRef.h',
				'src/lazy\SkDiscardableMemoryPool.cpp',
				'src/lazy\SkDiscardablePixelRef.cpp',
				'src/pathops/SkAddIntersections.cpp',
				'src/pathops/SkAddIntersections.h',
				'src/pathops/SkDCubicIntersection.cpp',
				'src/pathops/SkDCubicLineIntersection.cpp',
				'src/pathops/SkDCubicToQuads.cpp',
				'src/pathops/SkDLineIntersection.cpp',
				'src/pathops/SkDQuadImplicit.cpp',
				'src/pathops/SkDQuadImplicit.h',
				'src/pathops/SkDQuadIntersection.cpp',
				'src/pathops/SkDQuadLineIntersection.cpp',
				'src/pathops/SkIntersectionHelper.h',
				'src/pathops/SkIntersections.cpp',
				'src/pathops/SkIntersections.h',
				'src/pathops/SkLineParameters.h',
				'src/pathops/SkOpAngle.cpp',
				'src/pathops/SkOpAngle.h',
				'src/pathops/SkOpContour.cpp',
				'src/pathops/SkOpContour.h',
				'src/pathops/SkOpEdgeBuilder.cpp',
				'src/pathops/SkOpEdgeBuilder.h',
				'src/pathops/SkOpSegment.cpp',
				'src/pathops/SkOpSegment.h',
				'src/pathops/SkOpSpan.h',
				'src/pathops/SkPathOpsBounds.cpp',
				'src/pathops/SkPathOpsBounds.h',
				'src/pathops/SkPathOpsCommon.cpp',
				'src/pathops/SkPathOpsCommon.h',
				'src/pathops/SkPathOpsCubic.cpp',
				'src/pathops/SkPathOpsCubic.h',
				'src/pathops/SkPathOpsCurve.h',
				'src/pathops/SkPathOpsDebug.cpp',
				'src/pathops/SkPathOpsDebug.h',
				'src/pathops/SkPathOpsLine.cpp',
				'src/pathops/SkPathOpsLine.h',
				'src/pathops/SkPathOpsOp.cpp',
				'src/pathops/SkPathOpsPoint.cpp',
				'src/pathops/SkPathOpsPoint.h',
				'src/pathops/SkPathOpsQuad.cpp',
				'src/pathops/SkPathOpsQuad.h',
				'src/pathops/SkPathOpsRect.cpp',
				'src/pathops/SkPathOpsRect.h',
				'src/pathops/SkPathOpsSimplify.cpp',
				'src/pathops/SkPathOpsTightBounds.cpp',
				'src/pathops/SkPathOpsTriangle.cpp',
				'src/pathops/SkPathOpsTriangle.h',
				'src/pathops/SkPathOpsTypes.cpp',
				'src/pathops/SkPathOpsTypes.h',
				'src/pathops/SkPathWriter.cpp',
				'src/pathops/SkPathWriter.h',
				'src/pathops/SkQuarticRoot.cpp',
				'src/pathops/SkQuarticRoot.h',
				'src/pathops/SkReduceOrder.cpp',
				'src/pathops/SkReduceOrder.h',
				'src/effects/Sk1DPathEffect.cpp',
				'src/effects/Sk2DPathEffect.cpp',
				'src/effects/SkAlphaThresholdFilter.cpp',
				'src/effects/SkArithmeticMode.cpp',
				'src/effects/SkAvoidXfermode.cpp',
				'src/effects/SkBitmapSource.cpp',
				'src/effects/SkBlurDrawLooper.cpp',
				'src/effects/SkBlurImageFilter.cpp',
				'src/effects/SkBlurMask.cpp',
				'src/effects/SkBlurMask.h',
				'src/effects/SkBlurMaskFilter.cpp',
				'src/effects/SkColorFilterImageFilter.cpp',
				'src/effects/SkColorFilters.cpp',
				'src/effects/SkColorMatrix.cpp',
				'src/effects/SkColorMatrixFilter.cpp',
				'src/effects/SkComposeImageFilter.cpp',
				'src/effects/SkCornerPathEffect.cpp',
				'src/effects/SkDashPathEffect.cpp',
				'src/effects/SkDiscretePathEffect.cpp',
				'src/effects/SkDisplacementMapEffect.cpp',
				'src/effects/SkDropShadowImageFilter.cpp',
				'src/effects/SkEmbossMask.cpp',
				'src/effects/SkEmbossMask.h',
				'src/effects/SkEmbossMask_Table.h',
				'src/effects/SkEmbossMaskFilter.cpp',
				'src/effects/SkGpuBlurUtils.cpp',
				'src/effects/SkGpuBlurUtils.h',
				'src/effects/SkLayerDrawLooper.cpp',
				'src/effects/SkLayerRasterizer.cpp',
				'src/effects/SkLerpXfermode.cpp',
				'src/effects/SkLightingImageFilter.cpp',
				'src/effects/SkLumaColorFilter.cpp',
				'src/effects/SkMagnifierImageFilter.cpp',
				'src/effects/SkMatrixConvolutionImageFilter.cpp',
				'src/effects/SkMatrixImageFilter.cpp',
				'src/effects/SkMergeImageFilter.cpp',
				'src/effects/SkMorphologyImageFilter.cpp',
				'src/effects/SkOffsetImageFilter.cpp',
				'src/effects/SkPaintFlagsDrawFilter.cpp',
				'src/effects/SkPerlinNoiseShader.cpp',
				'src/effects/SkPictureImageFilter.cpp',
				'src/effects/SkPixelXorXfermode.cpp',
				'src/effects/SkPorterDuff.cpp',
				'src/effects/SkRectShaderImageFilter.cpp',
				'src/effects/SkTableColorFilter.cpp',
				'src/effects/SkTableMaskFilter.cpp',
				'src/effects/SkTestImageFilters.cpp',
				'src/effects/SkTileImageFilter.cpp',
				'src/effects/SkTransparentShader.cpp',
				'src/effects/SkXfermodeImageFilter.cpp',
				'src/effects/gradients/SkClampRange.cpp',
				'src/effects/gradients/SkClampRange.h',
				'src/effects/gradients/SkGradientBitmapCache.cpp',
				'src/effects/gradients/SkGradientBitmapCache.h',
				'src/effects/gradients/SkGradientShader.cpp',
				'src/effects/gradients/SkGradientShaderPriv.h',
				'src/effects/gradients/SkLinearGradient.cpp',
				'src/effects/gradients/SkLinearGradient.h',
				'src/effects/gradients/SkRadialGradient.cpp',
				'src/effects/gradients/SkRadialGradient.h',
				'src/effects/gradients/SkRadialGradient_Table.h',
				'src/effects/gradients/SkSweepGradient.cpp',
				'src/effects/gradients/SkSweepGradient.h',
				'src/effects/gradients/SkTwoPointConicalGradient.cpp',
				'src/effects/gradients/SkTwoPointConicalGradient.h',
				'src/effects/gradients/SkTwoPointConicalGradient_gpu.cpp',
				'src/effects/gradients/SkTwoPointConicalGradient_gpu.h',
				'src/effects/gradients/SkTwoPointRadialGradient.cpp',
				'src/effects/gradients/SkTwoPointRadialGradient.h',
				'src/opts/opts_check_x86.cpp',
				'src/opts/SkBitmapFilter_opts_SSE2.cpp',
				'src/opts/SkBitmapProcState_opts_SSE2.cpp',
				'src/opts/SkBitmapProcState_opts_SSSE3.cpp',
				'src/opts/SkBlitRect_opts_SSE2.cpp',
				'src/opts/SkBlitRow_opts_SSE2.cpp',
				'src/opts/SkBlurImage_opts_SSE2.cpp',
				'src/opts/SkBlurImage_opts_SSE4.cpp',
				'src/opts/SkMorphology_opts_SSE2.cpp',
				'src/opts/SkTextureCompression_opts_none.cpp',
				'src/opts/SkUtils_opts_SSE2.cpp',
				'src/opts/SkXfermode_opts_SSE2.cpp',
				'src/ports/SkAtomics_sync.h',
				'src/ports/SkAtomics_win.h',
				'src/ports/SkDebug_win.cpp',
				'src/ports/SkDiscardableMemory_none.cpp',
				'src/ports/SkFontHost_win.cpp',
				'src/ports/SkGlobalInitialization_default.cpp',
				'src/ports/SkMemory_malloc.cpp',
				'src/ports/SkMutex_win.h',
				'src/ports/SkOSFile_stdio.cpp',
				'src/ports/SkOSFile_win.cpp',
				'src/ports/SkTime_win.cpp',
				'src/ports/SkTLS_win.cpp',
				'src/ports/SkFontMgr_default_gdi.cpp',
				'src/gpu/GrAAConvexPathRenderer.cpp',
				'src/gpu/GrAAConvexPathRenderer.h',
				'src/gpu/GrAAHairLinePathRenderer.cpp',
				'src/gpu/GrAAHairLinePathRenderer.h',
				'src/gpu/GrAARectRenderer.cpp',
				'src/gpu/GrAARectRenderer.h',
				'src/gpu/GrAddPathRenderers_default.cpp',
				'src/gpu/GrAllocator.h',
				'src/gpu/GrAllocPool.cpp',
				'src/gpu/GrAllocPool.h',
				'src/gpu/GrAtlas.cpp',
				'src/gpu/GrAtlas.h',
				'include/gpu/GrBinHashKey.h',
				'src/gpu/GrBitmapTextContext.cpp',
				'src/gpu/GrBitmapTextContext.h',
				'src/gpu/GrBlend.cpp',
				'src/gpu/GrBlend.h',
				'src/gpu/GrBufferAllocPool.cpp',
				'src/gpu/GrBufferAllocPool.h',
				'src/gpu/GrCacheID.cpp',
				'src/gpu/GrClipData.cpp',
				'src/gpu/GrClipMaskCache.cpp',
				'src/gpu/GrClipMaskCache.h',
				'src/gpu/GrClipMaskManager.cpp',
				'src/gpu/GrClipMaskManager.h',
				'src/gpu/GrContext.cpp',
				'src/gpu/GrDefaultPathRenderer.cpp',
				'src/gpu/GrDefaultPathRenderer.h',
				'src/gpu/GrDistanceFieldTextContext.cpp',
				'src/gpu/GrDistanceFieldTextContext.h',
				'src/gpu/GrDrawState.cpp',
				'src/gpu/GrDrawState.h',
				'src/gpu/GrDrawTarget.cpp',
				'src/gpu/GrDrawTarget.h',
				'src/gpu/GrDrawTargetCaps.h',
				'src/gpu/GrFontScaler.cpp',
				'src/gpu/GrGeometryBuffer.h',
				'src/gpu/GrGpu.cpp',
				'src/gpu/GrGpu.h',
				'src/gpu/GrGpuFactory.cpp',
				'src/gpu/GrGpuResource.cpp',
				'src/gpu/GrIndexBuffer.h',
				'src/gpu/GrInOrderDrawBuffer.cpp',
				'src/gpu/GrInOrderDrawBuffer.h',
				'src/gpu/GrLayerCache.cpp',
				'src/gpu/GrLayerCache.h',
				'src/gpu/GrMemoryPool.cpp',
				'src/gpu/GrMemoryPool.h',
				'src/gpu/GrOrderedSet.h',
				'src/gpu/GrOvalRenderer.cpp',
				'src/gpu/GrOvalRenderer.h',
				'src/gpu/GrPaint.cpp',
				'src/gpu/GrPath.cpp',
				'src/gpu/GrPath.h',
				'src/gpu/GrPathRange.h',
				'src/gpu/GrPathRenderer.cpp',
				'src/gpu/GrPathRenderer.h',
				'src/gpu/GrPathRendererChain.cpp',
				'src/gpu/GrPathRendering.h',
				'src/gpu/GrPathUtils.cpp',
				'src/gpu/GrPathUtils.h',
				'src/gpu/GrPictureUtils.cpp',
				'src/gpu/GrPictureUtils.h',
				'src/gpu/GrPlotMgr.h',
				'src/gpu/GrRectanizer.h',
				'src/gpu/GrRectanizer_pow2.cpp',
				'src/gpu/GrRectanizer_pow2.h',
				'src/gpu/GrRectanizer_skyline.cpp',
				'src/gpu/GrRectanizer_skyline.h',
				'src/gpu/GrRedBlackTree.h',
				'src/gpu/GrReducedClip.cpp',
				'src/gpu/GrReducedClip.h',
				'src/gpu/GrRenderTarget.cpp',
				'src/gpu/GrResourceCache.cpp',
				'src/gpu/GrResourceCache.h',
				'src/gpu/GrResourceCache2.cpp',
				'src/gpu/GrResourceCache2.h',
				'src/gpu/GrRODrawState.cpp',
				'src/gpu/GrRODrawState.h',
				'src/gpu/GrSoftwarePathRenderer.cpp',
				'src/gpu/GrSoftwarePathRenderer.h',
				'src/gpu/GrStencil.cpp',
				'src/gpu/GrStencil.h',
				'src/gpu/GrStencilAndCoverPathRenderer.cpp',
				'src/gpu/GrStencilAndCoverPathRenderer.h',
				'src/gpu/GrStencilAndCoverTextContext.cpp',
				'src/gpu/GrStencilAndCoverTextContext.h',
				'src/gpu/GrStencilBuffer.cpp',
				'src/gpu/GrStencilBuffer.h',
				'src/gpu/GrStrokeInfo.h',
				'src/gpu/GrSurface.cpp',
				'src/gpu/GrSWMaskHelper.cpp',
				'src/gpu/GrSWMaskHelper.h',
				'src/gpu/GrTBSearch.h',
				'src/gpu/GrTemplates.h',
				'src/gpu/GrTextContext.cpp',
				'src/gpu/GrTextContext.h',
				'src/gpu/GrTextStrike.cpp',
				'src/gpu/GrTextStrike.h',
				'src/gpu/GrTextStrike_impl.h',
				'src/gpu/GrTexture.cpp',
				'src/gpu/GrTextureAccess.cpp',
				'src/gpu/GrTraceMarker.cpp',
				'src/gpu/GrTraceMarker.h',
				'src/gpu/GrTracing.h',
				'src/gpu/GrVertexBuffer.h',
				'src/gpu/SkGpuDevice.cpp',
				'src/gpu/SkGr.cpp',
				'src/gpu/GrProcessor.cpp',
				'src/gpu/GrProgramElement.cpp',
				'src/gpu/GrGpuResourceRef.cpp',
				'src/gpu/SkGrPixelRef.cpp',
				'src/gpu/SkGrTexturePixelRef.cpp',
				'src/gpu/GrPathRendering.cpp',
				'src/gpu/GrOptDrawState.cpp',
				'src/gpu/GrOptDrawState.h',
				'src/gpu/GrPathRange.cpp',
				'src/gpu/gl/GrGLAssembleInterface.cpp',
				'src/gpu/gl/GrGLAssembleInterface.h',
				'src/gpu/gl/GrGLBufferImpl.cpp',
				'src/gpu/gl/GrGLBufferImpl.h',
				'src/gpu/gl/GrGLCaps.cpp',
				'src/gpu/gl/GrGLCaps.h',
				'src/gpu/gl/GrGLContext.cpp',
				'src/gpu/gl/GrGLContext.h',
				'src/gpu/gl/GrGLCreateNullInterface.cpp',
				'src/gpu/gl/GrGLDefaultInterface_native.cpp',
				'src/gpu/gl/GrGLDefines.h',
				#'src/gpu/gl/GrGLEffect.h',
				'src/gpu/gl/GrGLExtensions.cpp',
				'src/gpu/gl/GrGLIndexBuffer.cpp',
				'src/gpu/gl/GrGLIndexBuffer.h',
				'src/gpu/gl/GrGLInterface.cpp',
				'src/gpu/gl/GrGLIRect.h',
				'src/gpu/gl/GrGLNameAllocator.cpp',
				'src/gpu/gl/GrGLNameAllocator.h',
				'src/gpu/gl/GrGLNoOpInterface.cpp',
				'src/gpu/gl/GrGLNoOpInterface.h',
				'src/gpu/gl/GrGLPath.cpp',
				'src/gpu/gl/GrGLPath.h',
				'src/gpu/gl/GrGLPathRange.cpp',
				'src/gpu/gl/GrGLPathRange.h',
				'src/gpu/gl/GrGLPathRendering.cpp',
				'src/gpu/gl/GrGLPathRendering.h',
				'src/gpu/gl/GrGLProgram.cpp',
				'src/gpu/gl/GrGLProgram.h',
				'src/gpu/gl/GrGLProgramDataManager.cpp',
				'src/gpu/gl/GrGLProgramDataManager.h',
				'src/gpu/gl/GrGLProgramDesc.cpp',
				'src/gpu/gl/GrGLProgramDesc.h',
				'src/gpu/gl/GrGLProgramEffects.cpp',
				'src/gpu/gl/GrGLProgramEffects.h',
				'src/gpu/gl/GrGLRenderTarget.cpp',
				'src/gpu/gl/GrGLRenderTarget.h',
				'src/gpu/gl/GrGLShaderVar.h',
				'src/gpu/gl/GrGLSL.cpp',
				'src/gpu/gl/GrGLSL.h',
				'src/gpu/gl/GrGLSL_impl.h',
				'src/gpu/gl/GrGLStencilBuffer.cpp',
				'src/gpu/gl/GrGLStencilBuffer.h',
				'src/gpu/gl/GrGLTexture.cpp',
				'src/gpu/gl/GrGLTexture.h',
				'src/gpu/gl/GrGLUniformHandle.h',
				'src/gpu/gl/GrGLUtil.cpp',
				'src/gpu/gl/GrGLUtil.h',
				'src/gpu/gl/GrGLVertexArray.cpp',
				'src/gpu/gl/GrGLVertexArray.h',
				'src/gpu/gl/GrGLVertexBuffer.cpp',
				'src/gpu/gl/GrGLVertexBuffer.h',
				#'src/gpu/gl/GrGLVertexEffect.h',
				'src/gpu/gl/GrGpuGL.cpp',
				'src/gpu/gl/GrGpuGL.h',
				'src/gpu/gl/GrGpuGL_program.cpp',
				'src/gpu/gl/SkGLContextHelper.cpp',
				'src/gpu/gl/SkNullGLContext.cpp',
				'src/gpu/gl/win/GrGLCreateNativeInterface_win.cpp',
				'src/gpu/gl/win/SkNativeGLContext_win.cpp',
				'src/gpu/gl/debug/GrBufferObj.cpp',
				'src/gpu/gl/debug/GrBufferObj.h',
				'src/gpu/gl/debug/GrDebugGL.cpp',
				'src/gpu/gl/debug/GrDebugGL.h',
				'src/gpu/gl/debug/GrFakeRefObj.h',
				'src/gpu/gl/debug/GrFBBindableObj.h',
				'src/gpu/gl/debug/GrFrameBufferObj.cpp',
				'src/gpu/gl/debug/GrFrameBufferObj.h',
				'src/gpu/gl/debug/GrGLCreateDebugInterface.cpp',
				'src/gpu/gl/debug/GrProgramObj.cpp',
				'src/gpu/gl/debug/GrProgramObj.h',
				'src/gpu/gl/debug/GrRenderBufferObj.h',
				'src/gpu/gl/debug/GrShaderObj.cpp',
				'src/gpu/gl/debug/GrShaderObj.h',
				'src/gpu/gl/debug/GrTextureObj.cpp',
				'src/gpu/gl/debug/GrTextureObj.h',
				'src/gpu/gl/debug/GrTextureUnitObj.cpp',
				'src/gpu/gl/debug/GrTextureUnitObj.h',
				'src/gpu/gl/debug/GrVertexArrayObj.h',
				'src/gpu/gl/debug/SkDebugGLContext.cpp',
				'src/gpu/gl/builders/GrGLFragmentShaderBuilder.cpp',
				'src/gpu/gl/builders/GrGLFragmentShaderBuilder.h',
				'src/gpu/gl/builders/GrGLGeometryShaderBuilder.cpp',
				'src/gpu/gl/builders/GrGLGeometryShaderBuilder.h',
				'src/gpu/gl/builders/GrGLProgramBuilder.cpp',
				'src/gpu/gl/builders/GrGLProgramBuilder.h',
				'src/gpu/gl/builders/GrGLShaderBuilder.cpp',
				'src/gpu/gl/builders/GrGLShaderBuilder.h',
				'src/gpu/gl/builders/GrGLShaderStringBuilder.cpp',
				'src/gpu/gl/builders/GrGLShaderStringBuilder.h',
				'src/gpu/gl/builders/GrGLSLPrettyPrint.cpp',
				'src/gpu/gl/builders/GrGLVertexShaderBuilder.cpp',
				'src/gpu/gl/builders/GrGLVertexShaderBuilder.h',
				'src/gpu/gl/builders/GrGLFullProgramBuilder.cpp',
				'src/gpu/gl/builders/GrGLFullProgramBuilder.h',
				'src/gpu/gl/builders/GrGLFragmentOnlyProgramBuilder.cpp',
				'src/gpu/gl/builders/GrGLFragmentOnlyProgramBuilder.h',
				
				'src/gpu/effects/Gr1DKernelEffect.h',
				'src/gpu/effects/GrBezierEffect.cpp',
				'src/gpu/effects/GrBezierEffect.h',
				'src/gpu/effects/GrBicubicEffect.cpp',
				'src/gpu/effects/GrBicubicEffect.h',
				'src/gpu/effects/GrConfigConversionEffect.cpp',
				'src/gpu/effects/GrConfigConversionEffect.h',
				'src/gpu/effects/GrConvexPolyEffect.cpp',
				'src/gpu/effects/GrConvexPolyEffect.h',
				'src/gpu/effects/GrConvolutionEffect.cpp',
				'src/gpu/effects/GrConvolutionEffect.h',
				'src/gpu/effects/GrCustomCoordsTextureEffect.cpp',
				'src/gpu/effects/GrCustomCoordsTextureEffect.h',
				'src/gpu/effects/GrDashingEffect.cpp',
				'src/gpu/effects/GrDashingEffect.h',
				'src/gpu/effects/GrDistanceFieldTextureEffect.cpp',
				'src/gpu/effects/GrDistanceFieldTextureEffect.h',
				'src/gpu/effects/GrDitherEffect.cpp',
				'src/gpu/effects/GrDitherEffect.h',
				'src/gpu/effects/GrMatrixConvolutionEffect.cpp',
				'src/gpu/effects/GrMatrixConvolutionEffect.h',
				'src/gpu/effects/GrOvalEffect.cpp',
				'src/gpu/effects/GrOvalEffect.h',
				'src/gpu/effects/GrRRectEffect.cpp',
				'src/gpu/effects/GrRRectEffect.h',
				'src/gpu/effects/GrSimpleTextureEffect.cpp',
				'src/gpu/effects/GrSimpleTextureEffect.h',
				'src/gpu/effects/GrSingleTextureEffect.cpp',
				'src/gpu/effects/GrSingleTextureEffect.h',
				'src/gpu/effects/GrTextureDomain.cpp',
				'src/gpu/effects/GrTextureDomain.h',
				'src/gpu/effects/GrTextureStripAtlas.cpp',
				'src/gpu/effects/GrTextureStripAtlas.h',
				'src/gpu/effects/GrYUVtoRGBEffect.cpp',
				'src/gpu/effects/GrYUVtoRGBEffect.h',
				'src/sfnt/SkOTTable_name.cpp',
				'src/sfnt/SkOTUtils.cpp',
				'src/images/SkImageDecoder.cpp',
				'src/images/SkImageEncoder.cpp',
				'src/images/SkImageEncoder_Factory.cpp',
				'include/core/SkAdvancedTypefaceMetrics.h',
				'include/core/SkBBHFactory.h',
				'include/core/SkBitmap.h',
				'include/core/SkBitmapDevice.h',
				'include/core/SkBlitRow.h',
				'include/core/SkCanvas.h',
				'include/core/SkChunkAlloc.h',
				'include/core/SkClipStack.h',
				'include/core/SkColor.h',
				'include/core/SkColorFilter.h',
				'include/core/SkColorPriv.h',
				'include/core/SkColorShader.h',
				'include/core/SkComposeShader.h',
				'include/core/SkData.h',
				'include/core/SkDeque.h',
				'include/core/SkDevice.h',
				'src/core/SkDeviceProperties.h',
				'include/core/SkDither.h',
				'include/core/SkDraw.h',
				'include/core/SkDrawFilter.h',
				'include/core/SkDrawLooper.h',
				'include/core/SkEndian.h',
				'include/core/SkError.h',
				'include/core/SkFixed.h',
				'include/core/SkFlattenable.h',
				'include/core/SkFlattenableSerialization.h',
				'include/core/SkFloatBits.h',
				'include/core/SkFloatingPoint.h',
				'include/core/SkFontHost.h',
				'include/core/SkGraphics.h',
				'include/core/SkImage.h',
				'include/core/SkImageDecoder.h',
				'include/core/SkImageEncoder.h',
				'include/core/SkImageFilter.h',
				'include/core/SkImageInfo.h',
				'include/core/SkInstCnt.h',
				'include/core/SkMallocPixelRef.h',
				'include/core/SkMask.h',
				'include/core/SkMaskFilter.h',
				'include/core/SkMath.h',
				'include/core/SkMatrix.h',
				'include/core/SkMetaData.h',
				'include/core/SkMultiPictureDraw.h',
				'include/core/SkOnce.h',
				'include/core/SkOSFile.h',
				'include/core/SkPackBits.h',
				'include/core/SkPaint.h',
				'include/core/SkPath.h',
				'include/core/SkPathEffect.h',
				'include/core/SkPathMeasure.h',
				'include/core/SkPathRef.h',
				'include/core/SkPicture.h',
				'include/core/SkPictureRecorder.h',
				'include/core/SkPixelRef.h',
				'include/core/SkPoint.h',
				'include/core/SkPreConfig.h',
				'include/core/SkRasterizer.h',
				'include/core/SkRect.h',
				'include/core/SkRefCnt.h',
				'include/core/SkRegion.h',
				'include/core/SkRRect.h',
				'include/core/SkScalar.h',
				'include/core/SkShader.h',
				'include/core/SkStream.h',
				'include/core/SkString.h',
				'include/core/SkStrokeRec.h',
				'include/core/SkSurface.h',
				'include/core/SkTArray.h',
				'include/core/SkTDArray.h',
				'include/core/SkTDict.h',
				'include/core/SkTDStack.h',
				'include/core/SkTemplates.h',
				'include/core/SkTextBlob.h',
				'include/core/SkThread.h',
				'include/core/SkTime.h',
				'include/core/SkTInternalLList.h',
				'include/core/SkTLazy.h',
				'include/core/SkTRegistry.h',
				'include/core/SkTSearch.h',
				'include/core/SkTypeface.h',
				'include/core/SkTypes.h',
				'include/core/SkUnPreMultiply.h',
				'include/core/SkUtils.h',
				'include/core/SkWeakRefCnt.h',
				'include/core/SkWriter32.h',
				'include/core/SkXfermode.h',
				'include/utils/SkBoundaryPatch.h',
				'include/utils/SkCamera.h',
				'include/utils/SkCanvasStateUtils.h',
				'include/utils/SkCubicInterval.h',
				'include/utils/SkCullPoints.h',
				'include/utils/SkDebugUtils.h',
				'include/utils/SkDumpCanvas.h',
				'include/utils/SkEventTracer.h',
				'include/utils/SkFrontBufferedStream.h',
				'include/utils/SkInterpolator.h',
				'include/utils/SkLayer.h',
				'include/utils/SkMatrix44.h',
				'include/utils/SkMeshUtils.h',
				'include/utils/SkNinePatch.h',
				'include/utils/SkNoSaveLayerCanvas.h',
				'include/utils/SkNullCanvas.h',
				'include/utils/SkNWayCanvas.h',
				'include/utils/SkParse.h',
				'include/utils/SkParsePaint.h',
				'include/utils/SkParsePath.h',
				'include/utils/SkPictureUtils.h',
				'include/utils/SkProxyCanvas.h',
				'include/utils/SkRandom.h',
				'include/utils/SkRTConf.h',
				'include/utils/SkWGL.h',
				'include/utils/win/SkAutoCoInitialize.h',
				'include/utils/win/SkHRESULT.h',
				'include/utils/win/SkIStream.h',
				'include/utils/win/SkTScopedComPtr.h',
				'include/utils/mac/SkCGUtils.h',
				'include/pathops/SkPathOps.h',
				'include/effects/Sk1DPathEffect.h',
				'include/effects/Sk2DPathEffect.h',
				'include/effects/SkAlphaThresholdFilter.h',
				'include/effects/SkArithmeticMode.h',
				'include/effects/SkAvoidXfermode.h',
				'include/effects/SkBitmapSource.h',
				'include/effects/SkBlurDrawLooper.h',
				'include/effects/SkBlurImageFilter.h',
				'include/effects/SkBlurMaskFilter.h',
				'include/effects/SkColorFilterImageFilter.h',
				'include/effects/SkColorMatrix.h',
				'include/effects/SkColorMatrixFilter.h',
				'include/effects/SkCornerPathEffect.h',
				'include/effects/SkDashPathEffect.h',
				'include/effects/SkDiscretePathEffect.h',
				'include/effects/SkDisplacementMapEffect.h',
				'include/effects/SkDrawExtraPathEffect.h',
				'include/effects/SkDropShadowImageFilter.h',
				'include/effects/SkEmbossMaskFilter.h',
				'include/effects/SkGradientShader.h',
				'include/effects/SkLayerDrawLooper.h',
				'include/effects/SkLayerRasterizer.h',
				'include/effects/SkLerpXfermode.h',
				'include/effects/SkLightingImageFilter.h',
				'include/effects/SkLumaColorFilter.h',
				'include/effects/SkMagnifierImageFilter.h',
				'include/effects/SkMorphologyImageFilter.h',
				'include/effects/SkOffsetImageFilter.h',
				'include/effects/SkPaintFlagsDrawFilter.h',
				'include/effects/SkPerlinNoiseShader.h',
				'include/effects/SkPixelXorXfermode.h',
				'include/effects/SkPorterDuff.h',
				'include/effects/SkRectShaderImageFilter.h',
				'include/effects/SkTableColorFilter.h',
				'include/effects/SkTableMaskFilter.h',
				'include/effects/SkTileImageFilter.h',
				'include/effects/SkTransparentShader.h',
				'include/effects/SkXfermodeImageFilter.h',
				'include/ports/SkFontConfigInterface.h',
				'include/ports/SkFontMgr.h',
				'include/ports/SkFontMgr_indirect.h',
				'include/ports/SkFontStyle.h',
				'include/ports/SkRemotableFontMgr.h',
				#'include/gpu/GrBackendEffectFactory.h',
				'include/gpu/GrClipData.h',
				'include/gpu/GrColor.h',
				'include/gpu/GrConfig.h',
				'include/gpu/GrContext.h',
				'include/gpu/GrContextFactory.h',
				'include/gpu/GrCoordTransform.h',
				#'include/gpu/GrEffect.h',
				#'include/gpu/GrEffectStage.h',
				#'include/gpu/GrEffectUnitTest.h',
				'include/gpu/GrFontScaler.h',
				'include/gpu/GrGlyph.h',
				'include/gpu/GrGpuResource.h',
				'include/gpu/GrPaint.h',
				'include/gpu/GrPathRendererChain.h',
				'include/gpu/GrRect.h',
				'include/gpu/GrRenderTarget.h',
				'include/gpu/GrSurface.h',
				#'include/gpu/GrTBackendEffectFactory.h',
				'include/gpu/GrTexture.h',
				'include/gpu/GrTextureAccess.h',
				'include/gpu/GrTypes.h',
				'include/gpu/GrUserConfig.h',
				#'include/gpu/SkGpuDevice.h',
				'include/gpu/SkGr.h',
				'include/gpu/SkGrPixelRef.h',
				'include/gpu/SkGrTexturePixelRef.h',
				'include/gpu/gl/GrGLConfig.h',
				'include/gpu/gl/GrGLExtensions.h',
				'include/gpu/gl/GrGLFunctions.h',
				'include/gpu/gl/GrGLInterface.h',
				'include/gpu/gl/GrGLSLPrettyPrint.h',
				'include/gpu/gl/SkDebugGLContext.h',
				'include/gpu/gl/SkGLContextHelper.h',
				'include/gpu/gl/SkMesaGLContext.h',
				'include/gpu/gl/SkNativeGLContext.h',
				'include/gpu/gl/SkNullGLContext.h',
				'include/gpu/gl/SkANGLEGLContext.h',
				'src/images/bmpdecoderhelper.h',
				'src/images/SkScaledBitmapSampler.h',
				'src/images/transform_scanline.h',


    ],
    'include_dirs': [ 
      '.',
			'include/config',
			'include/core',
		  'src/core',
			'include/gpu',
			'src/gpu',
			'include/images',
			'include/utils',
			'include/utils/win',
			'src/utils',
			'include/ports',
			'include/text',
			'include/effects',
			'src/sfnt',
			'include/pathops',
			'src/image',
			'src/opts',
			'src/lazy',
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
          'msvs_disabled_warnings': [
              4244,4800,4100
          ],
	      }
    }, # configurations
  },
}
