# stikpetP

<!-- badges: start -->
<!-- badges: end -->

The goal of stikpetP is to provide functions for statistical analysis of
surveys. The functions are documented with the formulas and references
used. The documentation can be best viewed online at: https://peterstatistics.com/Packages/python-docs/index.html

The functions are NOT optimized but are instead relatively easy to follow.
If you would look at the source code it is most often a combination of
if statements and for loops.

Of course I could have made mistakes, so use at own risk. 

## Installation

You can install the development version of stikpetP from
[GitHub](https://github.com/) with:

``` python
!pip install https://raw.githubusercontent.com/stikpet/stikpetP/main/stikpetP.tar.gz
import stikpetP as ps
```
## Version 0.0.3
Major upgrade with now also functions for bivariate analysis. 

|Function|Performs|Comment|
|--------|--------|-------|
|ts_alexander_govern_owa|Alexander-Govern One-Way ANOVA||
|ts_bhapkar|Bhapkar Test||
|ts_binomial_os|Binomial Test (one-sample)|inc. three methods to determine two-sided p-value|
|ts_box_owa|Box One-Way ANOVA||
|ts_brown_forsythe_owa|Brown-Forsythe One-Way ANOVA||
|ts_cochran_owa|Cochran One-Way ANOVA||
|ts_cochran_q|Cochran Q Test||
|ts_fisher|Fisher Exact Test|2x2 only|
|ts_fisher_owa|Fisher One-Way ANOVA / F-Test||
|ts_fligner_policello|Fligner-Policello Test|incl. option for ties and continuity correction|
|ts_freeman_tukey_gof|Freeman-Tukey Test of Goodness-of-Fit|incl. three versions of continuity correction|
|ts_freeman_tukey_ind|Freeman-Tukey Test of Independence|two different versions of this test,incl. three versions of continuity correction|
|ts_freeman_tukey_read|Freeman-Tukey-Read Test of Goodness-of-Fit|incl. three versions of continuity correction|
|ts_friedman|Friedman Test|three versions|
|ts_g_gof|G (Likelihood Ratio) Goodness-of-Fit Test|incl. three versions of continuity correction|
|ts_g_ind|G (Likelihood Ratio / Wilks) Test of Independence|incl. three versions of continuity correction|
|ts_ham_owa|Hartung-Agac-Makabi One-Way ANOVA||
|ts_james_owa|James One-Way ANOVA|first and second order|
|ts_kruskal_wallis|Kruskal-Wallis H Test|twelve versions, and option for ties correction|
|ts_mann_whitney|Mann-Whitney U Test / Wilcoxon Rank Sum Test|exact and approximate version. Incl. option for continuity correction|
|ts_mcnemar_bowker|(McNemar-)Bowker Test|incl. option for continuity correction|
|ts_mehrotra_owa|Mehrotra One-Way ANOVA||
|ts_mod_log_likelihood_gof|Mod-Log Likelihood Test of Goodness-of-Fit|incl. three versions of continuity correction|
|ts_mod_log_likelihood_ind|Mod-Log Likelihood Test of Independence|incl. three versions of continuity correction|
|ts_mood_median|Mood Median Test|seven versions, and three options for continuity correction.|
|ts_multinomial_gof|Multinomial Goodness-of-Fit Test||
|ts_neyman_gof|Neyman Test of Goodness-of-Fit|incl. three versions of continuity correction|
|ts_neyman_ind|Neyman Test Of Independence|incl. three versions of continuity correction|
|ts_ozdemir_kurt_owa|Özdemir-Kurt B2||
|ts_pearson_gof|Pearson Chi-Square Goodness-of-Fit Test|incl. three versions of continuity correction|
|ts_pearson_ind|Pearson Chi-Square Test of Independence|incl. three versions of continuity correction|
|ts_powerdivergence_gof|Power Divergence Gof Test|incl. three versions of continuity correction|
|ts_powerdivergence_ind|Power Divergence Test Of Independence|incl. three versions of continuity correction|
|ts_score_os|Score Test (one-sample)|incl. option for continuity correction|
|ts_scott_smith_owa|Scott-Smith One-Way ANOVA||
|ts_sign_os|Sign Test (one-sample)||
|ts_sign_ps|Sign Test (Paired Samples)|exact and approximate version|
|ts_stuart_maxwell|Stuart-Maxwell Test||
|ts_student_t_is|Student t Test (Independent Samples)||
|ts_student_t_os|Student t-Test (One-Sample)||
|ts_student_t_ps|Student t Test (Paired Samples)||
|ts_trimmed_mean_is|Trimmed/Yuen Mean Test (Independent Samples)|two versions for the standard error|
|ts_trimmed_mean_os|Trimmed/Yuen Mean Test (One Sample)|two versions for the standard error|
|ts_trinomial_os|Trinomial Test (one-sample)||
|ts_trinomial_ps|Trinomial Test (Paired Samples)||
|ts_wald_os|Wald Test (one-sample)|incl. option for continuity correction|
|ts_welch_owa|Welch One-Way ANOVA||
|ts_welch_t_is|Welch t Test (Independent Samples)||
|ts_wilcox_owa|Wilcox One-Way ANOVA||
|ts_wilcoxon_os|Wilcoxon Signed Rank Test (One-Sample)|four version, three options to deal with equal to median, and option for ties and continuity correction|
|ts_wilcoxon_ps|Wilcoxon Signed Rank Test (Paired Samples)|four version, three options to deal with equal to median, and option for ties and continuity correction|
|ts_z_is|Z Test (independent samples)||
|ts_z_os|Z Test (One-Sample)||
|ts_z_ps|Z-test (Paired Samples)||
|es_alt_ratio|Alternative Ratio||
|es_bag_s|Bennett-Alpert-Goldstein S||
|es_becker_clogg_r|Becker And Clogg Rho|two versions|
|es_bin_bin|Binary vs Binary Effect Sizes|85 different effect sizes|
|es_cohen_d|Cohen d||
|es_cohen_d_os|Cohen d'||
|es_cohen_d_ps|Cohen dz|option to use within correction|
|es_cohen_f|Cohen F||
|es_cohen_g|Cohen g||
|es_cohen_h_os|Cohen h'||
|es_cohen_kappa|Cohen Kappa||
|es_cohen_w|Cohen w||
|es_common_language_is|Common Language (CL/CLES) (Independent Samples)||
|es_common_language_ps|Common Language Effect Size (Paired-Samples)|two versions|
|es_cont_coeff|(Pearson) Contingency Coefficient|two versions|
|es_cramer_v_gof|Cramer's V for Goodness-of-Fit|option to use Bergsma correction|
|es_cramer_v_ind|Cramer's V for Test of Independence|option to use Bergsma correction|
|es_dominance|Dominance and a Vargha-Delaney A like effect size measure||
|es_epsilon_sq|Epsilon Squared||
|es_eta_sq|Eta Squared||
|es_freeman_theta|Freeman Theta||
|es_glass_delta|Glass Delta||
|es_goodman_kruskal_lambda|Goodman-Kruskal Lambda|four options to deal with ties|
|es_goodman_kruskal_tau|Goodman-Kruskal Tau||
|es_hedges_g_is|Hedges g / Cohen ds|five versions, and option to use weighted variance|
|es_hedges_g_os|Hedges g (one-sample)|four versions|
|es_hedges_g_ps|Hedges g (Paired Samples)|five versions, and option to use weighted variance|
|es_jbm_e|Johnston-Berry-Mielke E|two versions|
|es_jbm_r|Berry-Johnston-Mielke R||
|es_kendall_w|||
|es_odds_ratio|Odds Ratio||
|es_omega_sq|Omega Squared||
|es_phi|Pearson/Yule Phi Coefficient / Cole C2 / Mean Square Contingency||
|es_rmsse|Root Mean Square Standardized Effect Size||
|es_scott_pi|Scott Pi||
|es_theil_u|Theil U / Uncertainty Coefficient||
|es_tschuprow_t|Tschuprow T|incl. option for continuity correction|
|es_vargha_delaney_a|Vargha-Delaney A||
|r_goodman_kruskal_gamma|Goodman-Kruskal Gamma|three ase to choose from|
|r_kendall_tau|Kendall Tau|two versions, four tests, optional continuity correction|
|r_pearson|Pearson Product-Moment Correlation Coefficient|three versions, and two tests|
|r_point_biserial|Point Biserial Correlation Coefficient||
|r_rank_biserial_is|(Glass) Rank Biserial Correlation / Cliff Delta||
|r_rank_biserial_os|Rank biserial correlation coefficient (one-sample)||
|r_rosenthal|Rosenthal Correlation Coefficient||
|r_somers_d|Somers D||
|r_spearman_rho|Spearman Rho / Spearman Rank Correlation Coefficient|seven tests to choose from|
|r_stuart_tau|Stuart(-Kendall) Tau c||
|r_tetrachoric|Tetrachoric Correlation Coefficient|four methods|
|me_consensus|Consensus||
|me_mean|Mean|eight different means|
|me_median|Median|three options for tiebreaker|
|me_mode|Mode|two options in case all equal|
|me_mode_bin|Mode For Binned Data||
|me_quantiles|Quantiles|18 different methods, and option to create own|
|me_quartile_range|Interquartile Range, Semi-Interquartile Range and Mid-Quartile Range||
|me_quartiles|Quartiles / Hinges|20 different methods, and option to create own|
|me_qv|Measures Of Qualitative Variation|32 different measures|
|me_variation|Measures of Quantitative Variation|9 different measures|
|ph_binomial|Pairwise Binomial Test for Post-Hoc Analysis||
|ph_column_proportion|Column Proportion Test|two options for se method|
|ph_conover_iman|Conover-Iman Test (Kruskal-Wallis)||
|ph_dunn|Dunn Test (Kruskal-Wallis)||
|ph_dunn_q|Dunn Test (for Cochran Q test)||
|ph_friedman|Dunn, Conover, or Nemenyi after Friedman||
|ph_mann_whitney|Pairwise Mann-Whitney U Test||
|ph_mcnemar_co|McNemar Test - Collapsed||
|ph_mcnemar_pw|McNemar Test - Pairwise||
|ph_mood_median|Pairwise Mood-Median Test||
|ph_nemenyi|Nemenyi Test (Kruskal-Wallis)||
|ph_pairwise_is|Pairwise Independent Samples Test||
|ph_pairwise_ps|Pairwise Paired Samples Tests||
|ph_pairwise_t|Pairwise Student T||
|ph_residual|Residual Test||
|ph_sdcf|Steel-Dwass-Critchlow-Fligner Test||
|tab_cross|Cross Table / Contingency Table||
|tab_frequency|Frequency Table||
|tab_frequency_bins|Binned Frequency Table||
|tab_nbins|Number Of Bins|13 methods|


## Version 0.0.2

This contains all my functions for 'basic' univariate analysis, it has the following functions available:

Correlations

1. r_rank_biserial_os()
1. r_rosenthal()

Effect sizes

1. es_convert()
1. es_alt_ratio()
1. es_cohen_d_os()
1. es_cohen_g()
1. es_cohen_h_os()
1. es_cohen_w()
1. es_cramer_v_gof()
1. es_dominance()
1. es_hedges_g_os()
1. es_jbm_e()

Measures

1. me_concensus()
1. me_mean()
1. me_median()
1. me_mode()
1. me_mode_bin()
1. me_quartile_range()
1. me_quartiles()
1. me_qv()
1. me_variation_ratio()

Other Functions

1. ph_binomial()
1. tab_frequency()
1. tab_frequency_bins()
1. tab_nbins()
1. th_cohen_d()
1. th_cohen_g()
1. th_cohen_h()
1. th_cohen_w()
1. th_pearson_r()

Tests

1. ts_binomial_os()
1. ts_freeman_tukey_gof
1. ts_freeman_tukey_read()
1. ts_g_gof()
1. ts_mod_log_likelihood_gof()
1. ts_multinomial_gof()
1. ts_neyman_gof()
1. ts_pearson_gof()
1. ts_powerdivergence_gof()
1. ts_score_os()
1. ts_sign_os()
1. ts_student_t_os()
1. ts_trimmed_mean_os()
1. ts_trinomial_os()
1. ts_wald_os()
1. ts_wilcoxon_os()
1. ts_z_os()

Visualisations

1. vi_bar_dual_axis()
1. vi_bar_simple()
1. vi_bar_stacked_single()
1. vi_boxplot_single()
1. vi_cleveland_dot_plot
1. vi_dot_plot()
1. vi_histogram()
1. vi_pareto_chart()
1. vi_pie()
