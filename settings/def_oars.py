# encoding: utf8

# Import local files:
import rois as ROIS


# Brain:
# Whole brain:
brain_whole_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.brain, ROIS.lacrimal_r, ROIS.lacrimal_l, ROIS.cochlea_l, ROIS.cochlea_r, ROIS.skin_brain, ROIS.nasal_cavity]
# Partial brain:
brain_partial_oars = [ROIS.brain, ROIS.brainstem, ROIS.brainstem_core, ROIS.brainstem_surface, ROIS.optic_chiasm, ROIS.optic_nrv_l, ROIS.optic_nrv_r, ROIS.cochlea_l, ROIS.cochlea_r, 
	ROIS.hippocampus_l, ROIS.hippocampus_r, ROIS.lacrimal_l, ROIS.lacrimal_r, ROIS.lens_l, ROIS.lens_r, ROIS.pituitary, ROIS.skin_brain_5,ROIS.eye_l, ROIS.eye_r]
# Stereotactic brain:
brain_stereotactic_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.lacrimal_l, ROIS.lacrimal_r, ROIS.brain, ROIS.cochlea_l, ROIS.cochlea_r, ROIS.optic_nrv_l, ROIS.optic_nrv_r, ROIS.optic_chiasm, ROIS.pituitary, ROIS.hippocampus_l, ROIS.hippocampus_r, ROIS.brainstem, ROIS.skin_srt]


# Lung:
lung_oars = [ROIS.lung_r, ROIS.lung_l, ROIS.lungs, ROIS.spinal_canal, ROIS.esophagus, ROIS.heart]
# Stereotactic lung:
lung_stereotactic_oars = [ROIS.chestwall,  ROIS.greatves,  ROIS.trachea, ROIS.liver,  ROIS.stomach, ROIS.skin, ROIS.main_bronchus_r, ROIS.main_bronchus_l]


# Breast:
# Partial breast:
breast_part_oars = [ROIS.lung_r, ROIS.lung_l,  ROIS.lungs, ROIS.heart, ROIS.spinal_canal, ROIS.surgical_bed]
# Whole breast:
breast_whole_oars = [ROIS.lung_r, ROIS.lung_l,  ROIS.lungs, ROIS.heart, ROIS.spinal_canal]
# Regional breast (lymph nodes):
breast_reg_oars = [ROIS.lung_r, ROIS.lung_l,  ROIS.lungs, ROIS.heart, ROIS.spinal_canal, ROIS.breast_l_draft, ROIS.breast_r_draft, ROIS.thyroid, ROIS.esophagus, ROIS.liver]


# Prostate:
# Common:
prostate_common_oars = [ROIS.bladder, ROIS.bowel_space, ROIS.femoral_l, ROIS.femoral_r, ROIS.rectum]
# Prostate bed:
prostate_bed_oars = prostate_common_oars
# Prostate bed with nodes:
prostate_bed_nodes_oars = prostate_common_oars + [ROIS.cauda_equina]
# Curative intact prostate:
prostate_oars = prostate_common_oars + [ROIS.seed1, ROIS.seed2, ROIS.seed3]
# Curative intact prostate with nodes:
prostate_nodes_oars = prostate_common_oars + [ROIS.cauda_equina, ROIS.seed1, ROIS.seed2, ROIS.seed3]
# Palliative prostate:
prostate_palliative_oars = prostate_common_oars


# Rectum:
rectum_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bladder, ROIS.bowel_space]


# Bladder:
bladder_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bladder, ROIS.bowel_space, ROIS.rectum]


# Palliative:
# Head:
palliative_head_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.eye_l_prv, ROIS.eye_r_prv, ROIS.lens_l, ROIS.lens_r, ROIS.lens_l_prv, ROIS.lens_r_prv, ROIS.brain, ROIS.brainstem, ROIS.spinal_canal_head]
# Neck:
palliative_neck_oars = [ROIS.oral_cavity, ROIS.parotid_l, ROIS.parotid_r, ROIS.parotids, ROIS.spinal_canal_head, ROIS.submand_l, ROIS.submand_r, ROIS.submands]
# Thorax:
palliative_thorax_oars = [ROIS.heart, ROIS.lung_l, ROIS.lung_r, ROIS.lungs, ROIS.spinal_canal]
palliative_thorax_abdomen_oars = [ROIS.bowel_space, ROIS.heart, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.lung_l, ROIS.lung_r, ROIS.lungs, ROIS.spinal_canal]
# Abdomen:
palliative_abdomen_oars = [ROIS.bowel_space, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.spinal_canal]
# Abdomen and pelvis:
palliative_abdomen_pelvis_oars = [ROIS.bladder, ROIS.bowel_space, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.rectum, ROIS.spinal_canal]
# Pelvis:
palliative_pelvis_oars = [ROIS.bladder, ROIS.bowel_space, ROIS.rectum, ROIS.spinal_canal]
# Stereotactic, spine thorax:
palliative_stereotactic_thorax_oars = [ROIS.esophagus, ROIS.heart, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.lung_l, ROIS.lung_r, ROIS.lungs, ROIS.skin, ROIS.spinal_cord, ROIS.trachea]
# Stereotactic, spine pelvis:
palliative_stereotactic_spine_pelvis_oars = [ROIS.bladder, ROIS.cauda_equina, ROIS.colon, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.rectum, ROIS.skin, ROIS.small_bowel, ROIS.spinal_cord]
# Stereotactic, pelvis:
palliative_stereotactic_pelvis_oars = [ROIS.bladder, ROIS.cauda_equina, ROIS.colon, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.rectum, ROIS.skin, ROIS.small_bowel]
