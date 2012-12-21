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
static const char *ng0 = "/home/stud/wydlermi/stud/mixsig/gps-evaluator/vhdl/src/cnt32_a.vhd";
extern char *IEEE_P_1242562249;

char *ieee_p_1242562249_sub_1919365254_1242562249(char *, char *, char *, char *, int );


static void work_a_2242777456_2209494583_p_0(char *t0)
{
    char t12[16];
    char *t1;
    char *t2;
    unsigned char t3;
    unsigned char t4;
    char *t5;
    char *t6;
    char *t7;
    unsigned char t8;
    unsigned char t9;
    unsigned char t10;
    unsigned char t11;
    char *t13;
    char *t14;
    char *t15;
    char *t16;
    unsigned int t17;
    unsigned int t18;

LAB0:    xsi_set_current_line(10, ng0);
    t1 = (t0 + 684U);
    t2 = *((char **)t1);
    t3 = *((unsigned char *)t2);
    t4 = (t3 == (unsigned char)3);
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
LAB3:    xsi_set_current_line(17, ng0);
    t1 = (t0 + 1040U);
    t2 = *((char **)t1);
    t1 = (t0 + 1808);
    t5 = (t1 + 32U);
    t6 = *((char **)t5);
    t7 = (t6 + 32U);
    t13 = *((char **)t7);
    memcpy(t13, t2, 32U);
    xsi_driver_first_trans_fast_port(t1);
    t1 = (t0 + 1764);
    *((int *)t1) = 1;

LAB1:    return;
LAB2:    xsi_set_current_line(11, ng0);
    t1 = xsi_get_transient_memory(32U);
    memset(t1, 0, 32U);
    t5 = t1;
    memset(t5, (unsigned char)2, 32U);
    t6 = (t0 + 1040U);
    t7 = *((char **)t6);
    t6 = (t7 + 0);
    memcpy(t6, t1, 32U);
    goto LAB3;

LAB5:    xsi_set_current_line(13, ng0);
    t2 = (t0 + 776U);
    t6 = *((char **)t2);
    t10 = *((unsigned char *)t6);
    t11 = (t10 == (unsigned char)3);
    if (t11 != 0)
        goto LAB10;

LAB12:
LAB11:    goto LAB3;

LAB7:    t2 = (t0 + 592U);
    t5 = *((char **)t2);
    t8 = *((unsigned char *)t5);
    t9 = (t8 == (unsigned char)3);
    t3 = t9;
    goto LAB9;

LAB10:    xsi_set_current_line(14, ng0);
    t2 = (t0 + 1040U);
    t7 = *((char **)t2);
    t2 = (t0 + 3208U);
    t13 = ieee_p_1242562249_sub_1919365254_1242562249(IEEE_P_1242562249, t12, t7, t2, 1);
    t14 = (t0 + 1040U);
    t15 = *((char **)t14);
    t14 = (t15 + 0);
    t16 = (t12 + 12U);
    t17 = *((unsigned int *)t16);
    t18 = (1U * t17);
    memcpy(t14, t13, t18);
    goto LAB11;

}


extern void work_a_2242777456_2209494583_init()
{
	static char *pe[] = {(void *)work_a_2242777456_2209494583_p_0};
	xsi_register_didat("work_a_2242777456_2209494583", "isim/evaluator_e_isim_beh.exe.sim/work/a_2242777456_2209494583.didat");
	xsi_register_executes(pe);
}
