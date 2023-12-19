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
## Functions
The package has the following functions included:

|Function|Performs|comment|
|-------|---------|-----------|
|di_kendall_tau|Kendall Tau Distribution| |
|di_mpmf|Multinomial Distribution| |
|di_mwwcdf|Mann-Whitney-Wilcoxon Distribution| |
|di_scdf|Spearman Rho Distribution| |
|di_wcdf|Wilcoxon Distribution| |
|es_alt_ratio|Alternative Ratio| |
|es_bag_s|Bennett-Alpert-Goldstein S| |
|es_bin_bin|Effect Sizes for Binary vs. Binary incl. 85 measures|85 different effect sizes |
|es_cohen_d|Cohen d for one-way ANOVA| |
|es_cohen_d_os|Cohen d' (for one-sample)| |
|es_cohen_d_ps|Cohen d_z (for paired-samples)|option to use within correction |
|es_cohen_f|Cohen f| |
|es_cohen_g|Cohen g| |
|es_cohen_h_os|Cohen h'| |
|es_cohen_kappa|Cohen kappa| |
|es_cohen_w|Cohen w| |
|es_common_language_is|Common Language Effect Size (ind. Samples)| |
|es_common_language_ps|Common Language Effect Size (Paired Samples)|two versions |
|es_cont_coeff|Contingency Coefficient|two versions |
|es_convert|Convert one effect size to another| |
|es_cramer_v_gof|Cramér V (for goodness-of-fit)|option to use Bergsma correction |
|es_cramer_v_ind|Cramér V (for independence)|option to use Bergsma correction |
|es_dominance|Dominance| |
|es_epsilon_sq|Epsilon Squared| |
|es_eta_sq|Eta Squared| |
|es_freeman_theta|Freeman Theta| |
|es_glass_delta|Glass Delta| |
|es_goodman_kruskal_lambda|Goodman-Kruskal Lambda|four options to deal with ties |
|es_goodman_kruskal_tau|Goodman-Kruskal tau| |
|es_hedges_g_is|Hedges g (ind. samples)|five versions, and option to use weighted variance |
|es_hedges_g_os|Hedges g (one-sample)|four versions |
|es_hedges_g_ps|Hedges g (paired samples)|five versions, and option to use weighted variance |
|es_jbm_e|Johnston-Berry-Mielke E|two versions |
|es_jbm_r|Berry-Johnston-Mielke R| |
|es_kendall_w|Kendall w| |
|es_odds_ratio|Odds Ratio| |
|es_omega_sq|Omega Square| |
|es_pairwise_bin|pairwise binary effect sizes| |
|es_phi|Phi coefficient| |
|es_rmsse|Root Mean Square Standardized Effect Size| |
|es_scott_pi|Scott pi| |
|es_theil_u|Theil U| |
|es_tschuprow_t|Tschuprow T|incl. option for continuity correction |
|es_vargha_delaney_a|Vargha and Delaney A| |
|me_consensus|Consensus| |
|me_mean|Mean (incl. different types of means)|eight different means |
|me_median|Median|three options for tiebreaker |
|me_mode|Mode|two options in case all equal |
|me_mode_bin|Mode for binned data| |
|me_quantiles|Quantiles (incl. 18 different methods)|18 different methods, and option to create own |
|me_quartile_range|Quartile Ranges| |
|me_quartiles|Quartiles (incl. 20 different methods)|20 different methods, and option to create own |
|me_qv|Qualitative Variation (25 different measures)|32 different measures |
|me_variation|Quantitative Variation (8 different measures)|9 different measures |
|ph_binomial|Pairwise Binomial test| |
|ph_column_proportion|Column Proportion test|two options for se method |
|ph_conover_iman|Post-Hoc Conover-Iman Test| |
|ph_dunn|Post-Hoc Dunn test (after Kruskal-Wallis)| |
|ph_dunn_q|Post-Hoc Dunn test (after Cochran Q)| |
|ph_friedman|Post-Hoc Friedman test| |
|ph_mann_whitney|Pairwise Mann-Whitney U tests| |
|ph_mcnemar_co|Pairwise McNemar test (collapsing others)| |
|ph_mcnemar_pw|Pairwise McNemar test| |
|ph_mood_median|Pairwise Mood Median test| |
|ph_nemenyi|Post-Hoc Nemenyi Test| |
|ph_pairwise_is|Post-Hoc Pairwise Independent Samples Test| |
|ph_pairwise_ps|Post-Hoc Pairwise Paired Samples Tests| |
|ph_pairwise_t|Post-Hoc Pairwise Student T| |
|ph_residual|Post-Hoc Residual Test| |
|ph_sdcf|Post-Hoc Steel-Dwass-Critchlow-Fligner Test| |
|r_goodman_kruskal_gamma|Goodman-Kruskal Gamma|three ase to choose from |
|r_kendall_tau|Kendall Tau (a and b)|two versions, four tests, optional continuity correction |
|r_pearson|Pearson Correlation Coefficient|three versions, and two tests |
|r_point_biserial|Point Biserial Correlation Coefficient| |
|r_rank_biserial_is|(Glass) Rank Biserial Correlation / Cliff Delta| |
|r_rank_biserial_os|Rank biserial correlation coefficient (one-sample)| |
|r_rosenthal|Rosenthal Correlation Coefficient| |
|r_somers_d|Somers’ d| |
|r_spearman_rho|Spearman Rho / Rank Correlation Coefficient|seven tests to choose from |
|r_stuart_tau|Stuart Tau c / Kendall Tau c| |
|r_tetrachoric|Tetrachoric Correlation Coefficient|four methods |
|tab_cross|Cross Table / Contingency Table| |
|tab_frequency|Frequency Table| |
|tab_frequency_bins|Binned Frequency Table| |
|tab_nbins|Number of Bins|13 methods |
|th_cohen_d|Rules of Thumb for Cohen d| |
|th_cohen_g|Rule-of-Thumb for Cohen g| |
|th_cohen_h|Rule-of-Thumb for Cohen h| |
|th_cohen_w|Rule-of-Thumb for Cohen w| |
|th_odds_ratio|Rules of thumb for Odds Ratio| |
|th_pearson_r|Rules of Thumb for Pearson Correlation Coefficient| |
|th_yule_q|Rules of thumb for Yule Q| |
|ts_alexander_govern_owa|Alexander-Govern Test| |
|ts_bhapkar|Bhapkar Test| |
|ts_binomial_os|One-Sample Binomial Test|inc. three methods to determine two-sided p-value |
|ts_box_owa|Box F-Test| |
|ts_brown_forsythe_owa|Brown-Forsythe Means Test| |
|ts_cochran_owa|Cochran One-Way ANOVA| |
|ts_cochran_q|Cochran Q Test| |
|ts_fisher|Fisher Exact test|2x2 only |
|ts_fisher_owa|Fisher/Classic One-Way ANOVA / F-Test| |
|ts_fligner_policello|Fligner-Policello Test|incl. option for ties and continuity correction |
|ts_freeman_tukey_gof|Freeman-Tukey Test of Goodness-of-Fit|incl. three versions of continuity correction |
|ts_freeman_tukey_ind|Freeman-Tukey Test of Independence|two different versions of this test,incl. three versions of continuity correction |
|ts_freeman_tukey_read|Freeman-Tukey-Read Test of Goodness-of-Fit|incl. three versions of continuity correction |
|ts_friedman|Friedman Test|three versions |
|ts_g_gof|G (Likelihood Ratio) Test of Goodness-of-Fit|incl. three versions of continuity correction |
|ts_g_ind|G (Likelihood Ratio / Wilks) Test of Independence|incl. three versions of continuity correction |
|ts_ham_owa|Hartung-Argaç-Makambi Test| |
|ts_james_owa|James One-Way Test|first and second order |
|ts_kruskal_wallis|Kruskal-Wallis H Test|twelve versions, and option for ties correction |
|ts_mann_whitney|Mann-Whitney U Test|exact and approximate version. Incl. option for continuity correction |
|ts_mcnemar_bowker|(McNemar-)Bowker Test|incl. option for continuity correction |
|ts_mehrotra_owa|Mehrotra Test| |
|ts_mod_log_likelihood_gof|Mod-Log Likelihood Test of Goodness-of-Fit|incl. three versions of continuity correction |
|ts_mod_log_likelihood_ind|Mod-Log Likelihood Test of Independence|incl. three versions of continuity correction |
|ts_mood_median|Mood Median Test|seven versions, and three options for continuity correction. |
|ts_multinomial_gof|Exact Multinomial Test of Goodness-of-Fit| |
|ts_neyman_gof|Neyman Test of Goodness-of-Fit|incl. three versions of continuity correction |
|ts_neyman_ind|Neyman Test of Independence|incl. three versions of continuity correction |
|ts_ozdemir_kurt_owa|Özdemir-Kurt Test| |
|ts_pearson_gof|Pearson Chi-Square Test of Goodness-of-Fit|incl. three versions of continuity correction |
|ts_pearson_ind|Pearson Chi-Square Test of Independence|incl. three versions of continuity correction |
|ts_powerdivergence_gof|Power Divergence Goodness-of Fit Tests|incl. three versions of continuity correction |
|ts_powerdivergence_ind|Power Divergence Test of Independence|incl. three versions of continuity correction |
|ts_score_os|One-Sample Score Test|incl. option for continuity correction |
|ts_scott_smith_owa|Scott-Smith Test| |
|ts_sign_os|one-sample sign test| |
|ts_sign_ps|Paired Samples Sign Test|exact and approximate version |
|ts_stuart_maxwell|Stuart-Maxwell / Marginal Homogeneity Test| |
|ts_student_t_is|Student t Test (Independent Samples)| |
|ts_student_t_os|One-Sample Student t-Test| |
|ts_student_t_ps|Student t Test (Paired Samples)| |
|ts_trimmed_mean_is|Independent Samples Trimmed/Yuen Mean Test|two versions for the standard error |
|ts_trimmed_mean_os|One-Sample (Yuen or Yuen-Welch) Trimmed Mean Test|two versions for the standard error |
|ts_trinomial_os|One-Sample Trinomial Test| |
|ts_trinomial_ps|Trinomial Test (Paired Samples)| |
|ts_wald_os|One-Sample Wald Test|incl. option for continuity correction |
|ts_welch_owa|Welch One-Way ANOVA| |
|ts_welch_t_is|Welch t Test (Independent Samples)| |
|ts_wilcox_owa|Wilcox Test| |
|ts_wilcoxon_os|One-Sample Wilcoxon Signed Rank Test|four version, three options to deal with equal to median, and option for ties and continuity correction |
|ts_wilcoxon_ps|Paired Samples Wilcoxon Signed Rank Test|four version, three options to deal with equal to median, and option for ties and continuity correction |
|ts_z_is|Independent Samples Z Test| |
|ts_z_os|One-Sample Z Test| |
|ts_z_ps|Z-test (Paired Samples)| |
|vi_bar_clustered|Clustered / Multiple Bar Chart| |
|vi_bar_dual_axis|Dual-Axis Bar Chart| |
|vi_bar_simple|Simple Bar-Chart| |
|vi_bar_stacked_multiple|Multiple Stacked Bar-Chart| |
|vi_bar_stacked_single|Single Stacked Bar-Chart| |
|vi_boxplot_single|Box (and Whisker) Plot| |
|vi_boxplot_split|Split Box Plot| |
|vi_butterfly_chart|Butterfly Chart / Tornado Chart / Pyramid Chart| |
|vi_cleveland_dot_plot|Cleveland Dot Plot| |
|vi_dot_plot|Dot Plot| |
|vi_histogram|Histogram| |
|vi_histogram_split|Split Histogram| |
|vi_pareto_chart|Pareto Chart| |
|vi_pie|Pie Chart| |
|vi_spine_plot|Spine Plot| |



## Version 0.0.3
Major upgrade with now also functions for bivariate analysis. 


## Version 0.0.2

This contains all my functions for 'basic' univariate analysis.
