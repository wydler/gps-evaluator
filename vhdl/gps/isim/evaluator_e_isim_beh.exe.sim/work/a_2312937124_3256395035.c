/**********************************************************************/
/*   ____  ____                                                       */
/*  /   /\/   /                                                       */
/* /___/  \  /                                                        */
/* \   \   \/                                                       */
/*  \   \        Copyright (c) 2003-2009 Xilinx, Inc.                */
/*  /   /          All Right Reserved.                                 */
/* /---/   /\                                                         */
/* \   \  /  \                                                      */
/*  \___\/\___\                                                    */
/***********************************************************************/

/* This file is designed for use with ISim build 0xcd3868a6 */

#define XSI_HIDE_SYMBOL_SPEC true
#include "xsi.h"
#include <memory.h>
#ifdef __GNUC__
#include <stdlib.h>
#else
#include <malloc.h>
#define alloca _alloca
#endif
static const char *ng0 = "/home/stud/wydlermi/stud/mixsig/gps-evaluator/vhdl/src/zwh_shift64_a.vhd";
extern char *IEEE_P_1242562249;

char *ieee_p_1242562249_sub_2547962040_1242562249(char *, char *, char *, char *, int );


static void work_a_2312937124_3256395035_p_0(char *t0)
{
    char t18[16];
    char *t1;
    char *t2;
    unsigned char t3;
    unsigned char t4;
    char *t5;
    char *t6;
    char *t7;
    char *t8;
    char *t9;
    char *t10;
    unsigned char t11;
    unsigned char t12;
    unsigned char t13;
    unsigned char t14;
    unsigned int t15;
    unsigned int t16;
    unsigned int t17;

LAB0:    xsi_set_current_line(36, ng0);
    t1 = (t0 + 684U);
    t2 = *((char **)t1);
    t3 = *((unsigned char *)t2);
    t4 = (t3 == (unsigned char)2);
    if (t4 != 0)
        goto LAB2;

LAB4:    t1 = (t0 + 568U);
    t4 = xsi_signal_has_event(t1);
    if (t4 == 1)
        goto LAB7;

LAB8:    t3 = (unsigned char)0;

LAB9:    if (t3 != 0)
        goto LAB5;

LAB6:
LAB3:    t1 = (t0 + 2224);
    *((int *)t1) = 1;

LAB1:    return;
LAB2:    xsi_set_current_line(38, ng0);
    t1 = xsi_get_transient_memory(8U);
    memset(t1, 0, 8U);
    t5 = t1;
    memset(t5, (unsigned char)2, 8U);
    t6 = (t0 + 2268);
    t7 = (t6 + 32U);
    t8 = *((char **)t7);
    t9 = (t8 + 32U);
    t10 = *((char **)t9);
    memcpy(t10, t1, 8U);
    xsi_driver_first_trans_fast_port(t6);
    goto LAB3;

LAB5:    xsi_set_current_line(40, ng0);
    t2 = (t0 + 1236U);
    t6 = *((char **)t2);
    t13 = *((unsigned char *)t6);
    t14 = (t13 == (unsigned char)3);
    if (t14 != 0)
        goto LAB10;

LAB12:    t1 = (t0 + 1328U);
    t2 = *((char **)t1);
    t3 = *((unsigned char *)t2);
    t4 = (t3 == (unsigned char)3);
    if (t4 != 0)
        goto LAB13;

LAB14:
LAB11:    xsi_set_current_line(47, ng0);
    t1 = (t0 + 1500U);
    t2 = *((char **)t1);
    t15 = (63 - 7);
    t16 = (t15 * 1U);
    t17 = (0 + t16);
    t1 = (t2 + t17);
    t5 = (t0 + 2268);
    t6 = (t5 + 32U);
    t7 = *((char **)t6);
    t8 = (t7 + 32U);
    t9 = *((char **)t8);
    memcpy(t9, t1, 8U);
    xsi_driver_first_trans_fast_port(t5);
    goto LAB3;

LAB7:    t2 = (t0 + 592U);
    t5 = *((char **)t2);
    t11 = *((unsigned char *)t5);
    t12 = (t11 == (unsigned char)3);
    t3 = t12;
    goto LAB9;

LAB10:    xsi_set_current_line(41, ng0);
    t2 = (t0 + 960U);
    t7 = *((char **)t2);
    t2 = (t0 + 1500U);
    t8 = *((char **)t2);
    t15 = (63 - 63);
    t16 = (t15 * 1U);
    t17 = (0 + t16);
    t2 = (t8 + t17);
    memcpy(t2, t7, 32U);
    xsi_set_current_line(42, ng0);
    t1 = (t0 + 868U);
    t2 = *((char **)t1);
    t1 = (t0 + 1500U);
    t5 = *((char **)t1);
    t15 = (63 - 31);
    t16 = (t15 * 1U);
    t17 = (0 + t16);
    t1 = (t5 + t17);
    memcpy(t1, t2, 32U);
    goto LAB11;

LAB13:    xsi_set_current_line(45, ng0);
    t1 = (t0 + 1500U);
    t5 = *((char **)t1);
    t1 = (t0 + 4496U);
    t6 = ieee_p_1242562249_sub_2547962040_1242562249(IEEE_P_1242562249, t18, t5, t1, 8);
    t7 = (t0 + 1500U);
    t8 = *((char **)t7);
    t7 = (t8 + 0);
    t9 = (t18 + 12U);
    t15 = *((unsigned int *)t9);
    t16 = (1U * t15);
    memcpy(t7, t6, t16);
    goto LAB11;

}


extern void work_a_2312937124_3256395035_init()
{
	static char *pe[] = {(void *)work_a_2312937124_3256395035_p_0};
	xsi_register_didat("work_a_2312937124_3256395035", "isim/evaluator_e_isim_beh.exe.sim/work/a_2312937124_3256395035.didat");
	xsi_register_executes(pe);
}
