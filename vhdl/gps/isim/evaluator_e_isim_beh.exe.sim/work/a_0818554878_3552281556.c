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
static const char *ng0 = "/home/stud/wydlermi/stud/mixsig/gps-evaluator/vhdl/src/clkcntsrl_a.vhd";
extern char *IEEE_P_1242562249;

unsigned char ieee_p_1242562249_sub_1781471956_1242562249(char *, char *, char *, int );
unsigned char ieee_p_1242562249_sub_1781543830_1242562249(char *, char *, char *, int );
char *ieee_p_1242562249_sub_1919365254_1242562249(char *, char *, char *, char *, int );


static void work_a_0818554878_3552281556_p_0(char *t0)
{
    char t19[16];
    char *t1;
    char *t2;
    unsigned char t3;
    unsigned char t4;
    char *t5;
    char *t6;
    char *t7;
    char *t8;
    unsigned char t9;
    unsigned char t10;
    unsigned char t11;
    unsigned char t12;
    unsigned char t13;
    unsigned char t14;
    char *t15;
    char *t16;
    char *t17;
    char *t18;
    unsigned int t20;
    unsigned int t21;

LAB0:    xsi_set_current_line(78, ng0);
    t1 = (t0 + 960U);
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
LAB3:    xsi_set_current_line(92, ng0);
    t1 = (t0 + 1512U);
    t2 = *((char **)t1);
    t3 = *((unsigned char *)t2);
    t1 = (t0 + 2672);
    t5 = (t1 + 32U);
    t6 = *((char **)t5);
    t7 = (t6 + 32U);
    t8 = *((char **)t7);
    *((unsigned char *)t8) = t3;
    xsi_driver_first_trans_fast_port(t1);
    t1 = (t0 + 2592);
    *((int *)t1) = 1;

LAB1:    return;
LAB2:    xsi_set_current_line(79, ng0);
    t1 = (t0 + 2636);
    t5 = (t1 + 32U);
    t6 = *((char **)t5);
    t7 = (t6 + 32U);
    t8 = *((char **)t7);
    *((unsigned char *)t8) = (unsigned char)2;
    xsi_driver_first_trans_fast(t1);
    xsi_set_current_line(80, ng0);
    t1 = xsi_get_transient_memory(9U);
    memset(t1, 0, 9U);
    t2 = t1;
    memset(t2, (unsigned char)3, 9U);
    t5 = (t0 + 1868U);
    t6 = *((char **)t5);
    t5 = (t6 + 0);
    memcpy(t5, t1, 9U);
    goto LAB3;

LAB5:    xsi_set_current_line(82, ng0);
    t2 = (t0 + 1696U);
    t6 = *((char **)t2);
    t12 = *((unsigned char *)t6);
    t13 = (t12 == (unsigned char)3);
    if (t13 == 1)
        goto LAB13;

LAB14:    t11 = (unsigned char)0;

LAB15:    if (t11 != 0)
        goto LAB10;

LAB12:    t1 = (t0 + 1604U);
    t2 = *((char **)t1);
    t4 = *((unsigned char *)t2);
    t9 = (t4 == (unsigned char)3);
    if (t9 == 1)
        goto LAB18;

LAB19:    t3 = (unsigned char)0;

LAB20:    if (t3 != 0)
        goto LAB16;

LAB17:    xsi_set_current_line(89, ng0);
    t1 = (t0 + 2636);
    t2 = (t1 + 32U);
    t5 = *((char **)t2);
    t6 = (t5 + 32U);
    t7 = *((char **)t6);
    *((unsigned char *)t7) = (unsigned char)2;
    xsi_driver_first_trans_fast(t1);

LAB11:    goto LAB3;

LAB7:    t2 = (t0 + 592U);
    t5 = *((char **)t2);
    t9 = *((unsigned char *)t5);
    t10 = (t9 == (unsigned char)3);
    t3 = t10;
    goto LAB9;

LAB10:    xsi_set_current_line(83, ng0);
    t8 = (t0 + 2636);
    t15 = (t8 + 32U);
    t16 = *((char **)t15);
    t17 = (t16 + 32U);
    t18 = *((char **)t17);
    *((unsigned char *)t18) = (unsigned char)3;
    xsi_driver_first_trans_fast(t8);
    xsi_set_current_line(84, ng0);
    t1 = (t0 + 1868U);
    t2 = *((char **)t1);
    t1 = (t0 + 5536U);
    t5 = ieee_p_1242562249_sub_1919365254_1242562249(IEEE_P_1242562249, t19, t2, t1, 1);
    t6 = (t0 + 1868U);
    t7 = *((char **)t6);
    t6 = (t7 + 0);
    t8 = (t19 + 12U);
    t20 = *((unsigned int *)t8);
    t21 = (1U * t20);
    memcpy(t6, t5, t21);
    goto LAB11;

LAB13:    t2 = (t0 + 1868U);
    t7 = *((char **)t2);
    t2 = (t0 + 5536U);
    t14 = ieee_p_1242562249_sub_1781471956_1242562249(IEEE_P_1242562249, t7, t2, 8);
    t11 = t14;
    goto LAB15;

LAB16:    xsi_set_current_line(86, ng0);
    t6 = xsi_get_transient_memory(9U);
    memset(t6, 0, 9U);
    t7 = t6;
    memset(t7, (unsigned char)2, 9U);
    t8 = (t0 + 1868U);
    t15 = *((char **)t8);
    t8 = (t15 + 0);
    memcpy(t8, t6, 9U);
    xsi_set_current_line(87, ng0);
    t1 = (t0 + 2636);
    t2 = (t1 + 32U);
    t5 = *((char **)t2);
    t6 = (t5 + 32U);
    t7 = *((char **)t6);
    *((unsigned char *)t7) = (unsigned char)3;
    xsi_driver_first_trans_fast(t1);
    goto LAB11;

LAB18:    t1 = (t0 + 1868U);
    t5 = *((char **)t1);
    t1 = (t0 + 5536U);
    t10 = ieee_p_1242562249_sub_1781543830_1242562249(IEEE_P_1242562249, t5, t1, 7);
    t3 = t10;
    goto LAB20;

}


extern void work_a_0818554878_3552281556_init()
{
	static char *pe[] = {(void *)work_a_0818554878_3552281556_p_0};
	xsi_register_didat("work_a_0818554878_3552281556", "isim/evaluator_e_isim_beh.exe.sim/work/a_0818554878_3552281556.didat");
	xsi_register_executes(pe);
}
