#ifndef _SOUI_HBOX_LAYOUT_H
#define _SOUI_HBOX_LAYOUT_H

#pragma once
#include "core/SWnd.h" 
#include "core/SPanel.h"
#include "core/Accelerator.h"

namespace SOUI
{

/**
 * @class      SHBox
 * @brief      ˮƽ��ʽ������
 *  
 */

	class SOUI_EXP SHBox : public SPanel
    {
        SOUI_CLASS_NAME(SHBox, L"hbox")
    public:
        SHBox();
        virtual ~SHBox() {}

        CSize GetViewSize();

        void SetViewSize(CSize szView);

        CPoint GetViewOrigin();

        void SetViewOrigin(CPoint pt);

				int EstimateViewSize();
    protected:
        void OnSize(UINT nType,CSize size);
    protected:
        virtual void OnViewSizeChanged(CSize szOld,CSize szNew);
        virtual void OnViewOriginChanged(CPoint ptOld,CPoint ptNew);

    protected:
        virtual CRect GetChildrenLayoutRect();

        virtual BOOL OnScroll(BOOL bVertical,UINT uCode,int nPos);

        virtual void UpdateScrollBar();
    protected:
        SOUI_ATTRS_BEGIN()
            ATTR_INT(L"viewwid", m_szView.cx, FALSE)
            ATTR_INT(L"viewhei", m_szView.cy, FALSE)
            ATTR_INT(L"origin-x", m_ptOrigin.x, FALSE)
            ATTR_INT(L"origin-y", m_ptOrigin.y, FALSE)
            ATTR_SIZE(L"viewSize",m_szView,FALSE)
        SOUI_ATTRS_END()

        SOUI_MSG_MAP_BEGIN()
            MSG_WM_SIZE(OnSize)
        SOUI_MSG_MAP_END()
    protected:
        CSize m_szView;
        CPoint m_ptOrigin;
		int m_nEstimateWidth;
    };

}

#endif