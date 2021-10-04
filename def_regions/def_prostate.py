# encoding: utf8

# Import local files:
import colors as COLORS
import def_oars as DEF
import margins as MARGINS
import roi as ROI
import rois as ROIS

# Definitions script for prostate treatments (prostate/prostate bed, with or without lymph nodes, normo/hypofractionated).
class DefProstate(object):

  # Adds target and OAR ROIs to the given site and creates them in RayStation.
  def __init__(self, pm, examination, ss, choices, site):
    # Choice 1: Region - prostate or bed?
    region = choices[1]
    if region == 'prostate':
      # Prostate:
      # Choice 2: Fractionation - normo or hypo?
      frac = choices[2]
      if frac == 'normo':
        # Conventionally fractionated prostate with vesicles (2.2Gy x 35):
        # Choice 3: Nodes - included or not?
        nodes = choices[3]
        # Targets:
        ctv_77 = ROI.ROIExpanded(ROIS.ctv_77.name, ROIS.ctv_77.type, COLORS.ctv_high, source = ROIS.prostate)
        ptv_77 = ROI.ROIExpanded(ROIS.ptv_77.name, ROIS.ptv_77.type, COLORS.ptv_high, source = ROIS.prostate, margins = MARGINS.prostate_seed_expansion)
        # OARs:
        bladder_ptv = ROI.ROIAlgebra(ROIS.z_bladder.name, ROIS.z_bladder.type, COLORS.bladder, sourcesA = [ROIS.bladder], sourcesB = [ptv_77], operator='Subtraction', marginsB = MARGINS.uniform_3mm_expansion)
        rectum_ptv = ROI.ROIAlgebra(ROIS.z_rectum.name, ROIS.z_rectum.type, COLORS.rectum, sourcesA = [ROIS.rectum], sourcesB = [ptv_77], operator='Subtraction', marginsB = MARGINS.uniform_2mm_expansion)
        wall_ptv_77 = ROI.ROIWall(ROIS.z_ptv_77_wall.name, ROIS.z_ptv_77_wall.type, COLORS.wall, ptv_77, 0.5, 0)
        if nodes == 'no':
          # Prostate only:
          # Targets:
          ctv_70 = ROI.ROIAlgebra(ROIS.ctv_70_sib.name, ROIS.ctv_70.type, COLORS.ctv_med, sourcesA = [ROIS.vesicles], sourcesB = [ptv_77], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_70 = ROI.ROIAlgebra(ROIS.ptv_70_sib.name, ROIS.ptv_70.type, COLORS.ptv_med, sourcesA = [ROIS.vesicles], sourcesB = [ptv_77], operator = 'Subtraction', marginsA = MARGINS.uniform_8mm_expansion, marginsB = MARGINS.zero)
          ptv_70_77 = ROI.ROIAlgebra(ROIS.ptv_70_77.name, ROIS.ptv_70_77.type, COLORS.ptv_low, sourcesA = [ROIS.prostate], sourcesB = [ROIS.vesicles], marginsA = MARGINS.prostate_seed_expansion, marginsB = MARGINS.uniform_8mm_expansion)
          site.add_targets([ptv_70_77])
          # OARs:
          bladder_ptv.sourcesB.extend([ptv_70])
          rectum_ptv.sourcesB.extend([ptv_70])
          site.add_oars(DEF.prostate_oars + [bladder_ptv, rectum_ptv, wall_ptv_77])
        elif nodes == 'with_node':
          # Elective nodes (with positive node):
          # Targets:
          ctv_n = ROI.ROIExpanded(ROIS.ctv_n.name, ROIS.ctv_n.type, COLORS.pelvic_nodes, source = ROIS.gtv_n, margins = MARGINS.uniform_5mm_expansion)
          ptv_n = ROI.ROIExpanded(ROIS.ptv_n.name, ROIS.ptv_n.type, ROIS.ptv_n.color, source = ctv_n, margins = MARGINS.prostate_lymph_nodes_seed_expansion)
          ctv_70 = ROI.ROIAlgebra(ROIS.ctv_70_sib.name, ROIS.ctv_70.type, COLORS.ctv_med, sourcesA = [ROIS.vesicles, ctv_n], sourcesB = [ptv_77], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_semves = ROI.ROIAlgebra(ROIS.ptv_semves.name, ROIS.ptv_semves.type, COLORS.ptv_med, sourcesA = [ROIS.vesicles], sourcesB = [ptv_77], operator = 'Subtraction', marginsA = MARGINS.uniform_8mm_expansion, marginsB = MARGINS.zero)
          ptv_70 = ROI.ROIAlgebra(ROIS.ptv_70_sib.name, ROIS.ptv_70_sib.type, ROIS.ptv_70_sib.color, sourcesA = [ptv_semves, ptv_n], sourcesB = [ptv_77], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_70_77 = ROI.ROIAlgebra(ROIS.ptv_70_77.name, ROIS.ptv_70_77.type, COLORS.ptv_low, sourcesA = [ptv_70], sourcesB = [ptv_77], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_56 = ROI.ROIAlgebra(ROIS.ptv_56.name, ROIS.ptv_56.type, COLORS.ptv_low, sourcesA = [ROIS.pelvic_nodes], sourcesB = [ptv_77, ptv_70], operator = 'Subtraction', marginsA = MARGINS.prostate_lymph_nodes_seed_expansion, marginsB = MARGINS.zero)
          ctv_56 = ROI.ROIAlgebra(ROIS.ctv_56.name, ROIS.ctv_56.type, COLORS.ctv_low, sourcesA = [ROIS.pelvic_nodes], sourcesB = [ptv_77, ptv_70], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_56_70_77 = ROI.ROIAlgebra(ROIS.ptv_56_70_77.name, ROIS.ptv_56_70_77.type, COLORS.ptv_low, sourcesA = [ptv_56, ptv_70], sourcesB = [ptv_77], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          site.add_targets([ROIS.gtv_n, ROIS.pelvic_nodes, ctv_n, ctv_56, ptv_n, ptv_semves, ptv_56, ptv_70_77, ptv_56_70_77])
          # OARs:
          bladder_ptv.sourcesB.extend([ptv_70, ptv_56])
          rectum_ptv.sourcesB.extend([ptv_70, ptv_56])
          bowel_ptv = ROI.ROIAlgebra(ROIS.z_spc_bowel.name, ROIS.z_spc_bowel.type, COLORS.bowel_space, sourcesA = [ROIS.bowel_space], sourcesB = [ptv_77, ptv_70, ptv_56], operator='Subtraction', marginsB = MARGINS.uniform_3mm_expansion)
          wall_ptv_70_77 = ROI.ROIWall(ROIS.z_ptv_70_77_wall.name, ROIS.z_ptv_70_77_wall.type, COLORS.wall, ptv_70_77, 1, 0)
          site.add_oars(DEF.prostate_nodes_oars + [bladder_ptv, rectum_ptv, wall_ptv_77] + [bowel_ptv, wall_ptv_70_77])
        elif nodes == 'with':
          # Elective nodes:
          # Targets:
          ctv_70 = ROI.ROIAlgebra(ROIS.ctv_70_sib.name, ROIS.ctv_70.type, COLORS.ctv_med, sourcesA = [ROIS.vesicles], sourcesB = [ptv_77], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_70 = ROI.ROIAlgebra(ROIS.ptv_70_sib.name, ROIS.ptv_70.type, COLORS.ptv_med, sourcesA = [ROIS.vesicles], sourcesB = [ptv_77], operator = 'Subtraction', marginsA = MARGINS.uniform_8mm_expansion, marginsB = MARGINS.zero)
          ptv_70_77 = ROI.ROIAlgebra(ROIS.ptv_70_77.name, ROIS.ptv_70_77.type, COLORS.ptv_low, sourcesA = [ROIS.prostate], sourcesB = [ROIS.vesicles], marginsA = MARGINS.prostate_seed_expansion, marginsB = MARGINS.uniform_8mm_expansion)
          ptv_56 = ROI.ROIAlgebra(ROIS.ptv_56.name, ROIS.ptv_56.type, COLORS.ptv_low, sourcesA = [ROIS.pelvic_nodes], sourcesB = [ptv_77, ptv_70], operator = 'Subtraction', marginsA = MARGINS.prostate_lymph_nodes_seed_expansion, marginsB = MARGINS.zero)
          ctv_56 = ROI.ROIAlgebra(ROIS.ctv_56.name, ROIS.ctv_56.type, COLORS.ctv_low, sourcesA = [ROIS.pelvic_nodes], sourcesB = [ptv_77, ptv_70], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_56_70_77 = ROI.ROIAlgebra(ROIS.ptv_56_70_77.name, ROIS.ptv_56_70_77.type, COLORS.ptv_low, sourcesA = [ptv_56, ptv_70], sourcesB = [ptv_77], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          site.add_targets([ROIS.pelvic_nodes, ctv_56, ptv_56, ptv_70_77, ptv_56_70_77])
          # OARs:
          bladder_ptv.sourcesB.extend([ptv_70, ptv_56])
          rectum_ptv.sourcesB.extend([ptv_70, ptv_56])
          bowel_ptv = ROI.ROIAlgebra(ROIS.z_spc_bowel.name, ROIS.z_spc_bowel.type, COLORS.bowel_space, sourcesA = [ROIS.bowel_space], sourcesB = [ptv_77, ptv_70, ptv_56], operator='Subtraction', marginsB = MARGINS.uniform_3mm_expansion)
          wall_ptv_70_77 = ROI.ROIWall(ROIS.z_ptv_70_77_wall.name, ROIS.z_ptv_70_77_wall.type, COLORS.wall, ptv_70_77, 1, 0)
          site.add_oars(DEF.prostate_nodes_oars + [bladder_ptv, rectum_ptv, wall_ptv_77] + [bowel_ptv, wall_ptv_70_77])
        # Common ROIs for all conventional fractionation:
        site.add_targets([ROIS.prostate, ROIS.vesicles, ctv_77, ctv_70, ptv_77, ptv_70])
      elif frac == 'hypo_60':
        # Hypofractionated prostate with vesicles (3 Gy x 20):
        # Targets:
        ptv_57_60 = ROI.ROIAlgebra(ROIS.ptv_57_60.name, ROIS.ptv_57_60.type, COLORS.ptv_low, sourcesA = [ROIS.prostate], sourcesB = [ROIS.vesicles], marginsA = MARGINS.prostate_seed_expansion, marginsB = MARGINS.uniform_8mm_expansion)
        ptv_60 = ROI.ROIExpanded(ROIS.ptv_60.name, ROIS.ptv_60.type, COLORS.ptv_high, source = ROIS.prostate, margins = MARGINS.prostate_seed_expansion)
        ptv_57 = ROI.ROIAlgebra(ROIS.ptv_57.name, ROIS.ptv_57.type, COLORS.ptv_med, sourcesA = [ptv_57_60], sourcesB = [ptv_60], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        ctv_57_60 = ROI.ROIAlgebra(ROIS.ctv_57_60.name, ROIS.ctv_57_60.type, COLORS.ctv_low, sourcesA = [ROIS.prostate], sourcesB = [ROIS.vesicles], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        ctv_60 = ROI.ROIExpanded(ROIS.ctv_60.name, ROIS.ctv_60.type, COLORS.ctv_high, source = ROIS.prostate)
        ctv_57 = ROI.ROIAlgebra(ROIS.ctv_57.name, ROIS.ctv_57.type, COLORS.ctv_med, sourcesA = [ctv_57_60], sourcesB = [ptv_60], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        site.add_targets([ROIS.prostate, ROIS.vesicles, ctv_60, ctv_57, ctv_57_60, ptv_57_60, ptv_60, ptv_57])
        # OARs:
        bladder_ptv = ROI.ROIAlgebra(ROIS.z_bladder.name, ROIS.z_bladder.type, COLORS.bladder, sourcesA = [ROIS.bladder], sourcesB = [ptv_60, ptv_57], operator='Subtraction', marginsB = MARGINS.uniform_3mm_expansion)
        rectum_ptv = ROI.ROIAlgebra(ROIS.z_rectum.name, ROIS.z_rectum.type, COLORS.rectum, sourcesA = [ROIS.rectum], sourcesB = [ptv_60, ptv_57], operator='Subtraction', marginsB = MARGINS.uniform_2mm_expansion)
        wall_ptv_60 = ROI.ROIWall(ROIS.z_ptv_60_wall.name, ROIS.z_ptv_60_wall.type, COLORS.wall, ptv_60, 0.5, 0)
        wall_ptv_57_60 = ROI.ROIWall(ROIS.z_ptv_57_60_wall.name, ROIS.z_ptv_57_60_wall.type, COLORS.wall, ptv_57_60, 1, 0)
        site.add_oars(DEF.prostate_oars + [bladder_ptv, rectum_ptv, wall_ptv_60, wall_ptv_57_60])
      elif frac in ['hypo_55','palliative']:
        # STAMPEDE (2.75 Gy x 20) or palliative prostate (e.q. 3 Gy x 13):
        # Targets:
        ctv = ROI.ROIExpanded(ROIS.ctv.name, ROIS.ctv.type, COLORS.ctv_low, source = ROIS.prostate, margins = MARGINS.zero)
        if frac == 'hypo_55':
          # Assuming markers:
          ptv = ROI.ROIExpanded(ROIS.ptv.name, ROIS.ptv.type, COLORS.ptv_high, source = ctv, margins = MARGINS.prostate_seed_expansion)
        elif frac == 'palliative':
          # Assuming no markers:
          ptv = ROI.ROIExpanded(ROIS.ptv.name, ROIS.ptv.type, COLORS.ptv_high, source = ctv, margins = MARGINS.prostate_bone_match_expansion)
        site.add_targets([ROIS.prostate, ctv, ptv])
        # OARs:
        bladder_ptv = ROI.ROIAlgebra(ROIS.z_bladder.name, ROIS.z_bladder.type, COLORS.bladder, sourcesA = [ROIS.bladder], sourcesB = [ptv], operator='Subtraction', marginsB = MARGINS.uniform_3mm_expansion)
        rectum_ptv = ROI.ROIAlgebra(ROIS.z_rectum.name, ROIS.z_rectum.type, COLORS.rectum, sourcesA = [ROIS.rectum], sourcesB = [ptv], operator='Subtraction', marginsB = MARGINS.uniform_2mm_expansion)
        wall_ptv_55 = ROI.ROIWall(ROIS.z_ptv_wall.name, ROIS.z_ptv_wall.type, COLORS.wall, ptv, 1, 0)
        site.add_oars(DEF.prostate_palliative_oars + [bladder_ptv, rectum_ptv, wall_ptv_55])
    else:
      # Prostate bed:
      # Choice 2: Fractionation - normo or hypo?
      frac = choices[2]
      # Fractionation:
      if frac == 'normo':
        # Conventional fractionation (2 Gy):
        # Choice 3: Nodes - included or not?
        nodes = choices[3]
        if nodes == 'no':
          # Prostate bed only:
          # Targets:
          ctv_70 = ROI.ROIExpanded(ROIS.ctv_70.name, ROIS.ctv_70.type, COLORS.ctv_high, source = ROIS.ctv_sb)
          ptv_70 = ROI.ROIExpanded(ROIS.ptv_70.name, ROIS.ptv_70.type, COLORS.ptv, source = ctv_70, margins = MARGINS.prostate_bone_match_expansion)
          # OARs:
          bladder_ptv = ROI.ROIAlgebra(ROIS.z_bladder.name, ROIS.z_bladder.type, COLORS.bladder, sourcesA = [ROIS.bladder], sourcesB = [ptv_70], operator='Subtraction', marginsB = MARGINS.uniform_3mm_expansion)
          rectum_ptv = ROI.ROIAlgebra(ROIS.z_rectum.name, ROIS.z_rectum.type, COLORS.rectum, sourcesA = [ROIS.rectum], sourcesB = [ptv_70], operator='Subtraction', marginsB = MARGINS.uniform_2mm_expansion)
          site.add_oars(DEF.prostate_bed_oars + [bladder_ptv, rectum_ptv])
        else:
          # Elective nodes:
          if nodes == 'with':
            # Targets:
            ctv_70 = ROI.ROIExpanded(ROIS.ctv_70.name, ROIS.ctv_70.type, COLORS.ctv_high, source = ROIS.ctv_sb)
            ptv_70 = ROI.ROIExpanded(ROIS.ptv_70.name, ROIS.ptv_70.type, COLORS.ptv, source = ctv_70, margins = MARGINS.prostate_bone_match_expansion)
          else:
            # Elective nodes (with positive node):
            # Targets:
            ctv_n = ROI.ROIExpanded(ROIS.ctv_n.name, ROIS.ctv_n.type, COLORS.pelvic_nodes, source = ROIS.gtv_n, margins = MARGINS.uniform_5mm_expansion)
            ptv_n = ROI.ROIExpanded(ROIS.ptv_n.name, ROIS.ptv_n.type, ROIS.ptv_n.color, source = ctv_n, margins = MARGINS.uniform_5mm_expansion)
            ptv_sb = ROI.ROIExpanded(ROIS.ptv_sb.name, ROIS.ptv_sb.type, ROIS.ptv_sb.color, source = ROIS.ctv_sb, margins = MARGINS.prostate_bone_match_expansion)
            ctv_70 = ROI.ROIAlgebra(ROIS.ctv_70.name, ROIS.ctv_70.type, COLORS.ctv_med, sourcesA = [ROIS.ctv_sb], sourcesB = [ctv_n], operator = 'Union')
            ptv_70 = ROI.ROIAlgebra(ROIS.ptv_70.name, ROIS.ptv_70.type, COLORS.ptv, sourcesA = [ptv_sb], sourcesB = [ptv_n], operator = 'Union', marginsA = MARGINS.zero , marginsB = MARGINS.zero)
            site.add_targets([ROIS.gtv_n, ctv_n, ptv_n, ptv_sb])
          # Common for elective nodes (with or without positive node):
          # Targets:
          ctv_56 = ROI.ROIAlgebra(ROIS.ctv_56.name, ROIS.ctv_56.type, COLORS.ctv_low, sourcesA = [ROIS.pelvic_nodes], sourcesB = [ptv_70], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_56 = ROI.ROIAlgebra(ROIS.ptv_56.name, ROIS.ptv_56.type, COLORS.ptv_low, sourcesA = [ROIS.pelvic_nodes], sourcesB = [ptv_70], operator = 'Subtraction', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          ptv_56_70 = ROI.ROIAlgebra(ROIS.ptv_56_70.name, ROIS.ptv_56_70.type, COLORS.ptv_low, sourcesA = [ptv_56], sourcesB = [ptv_70], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          site.add_targets([ROIS.pelvic_nodes, ctv_56, ptv_56, ptv_56_70])
          # OARs:
          bladder_ptv = ROI.ROIAlgebra(ROIS.z_bladder.name, ROIS.z_bladder.type, COLORS.bladder, sourcesA = [ROIS.bladder], sourcesB = [ptv_70, ptv_56], operator='Subtraction', marginsB = MARGINS.uniform_3mm_expansion)
          rectum_ptv = ROI.ROIAlgebra(ROIS.z_rectum.name, ROIS.z_rectum.type, COLORS.rectum, sourcesA = [ROIS.rectum], sourcesB = [ptv_70, ptv_56], operator='Subtraction', marginsB = MARGINS.uniform_2mm_expansion)
          bowel_ptv = ROI.ROIAlgebra(ROIS.z_spc_bowel.name, ROIS.z_spc_bowel.type, COLORS.bowel_space, sourcesA = [ROIS.bowel_space], sourcesB = [ptv_70, ptv_56], operator='Subtraction', marginsB = MARGINS.uniform_3mm_expansion)
          wall_ptv_70 = ROI.ROIWall(ROIS.z_ptv_70_wall.name, ROIS.z_ptv_70_wall.type, COLORS.wall, ptv_70, 1, 0)
          wall_ptv_56_temp = ROI.ROIWall(ROIS.z_ptv_56_temp.name, ROIS.z_ptv_56_temp.type, COLORS.wall, ptv_56, 1, 0)
          wall_ptv_56 = ROI.ROIAlgebra(ROIS.z_ptv_56_wall.name, ROIS.z_ptv_56_wall.type, COLORS.wall, sourcesA = [wall_ptv_56_temp], sourcesB = [ptv_70, wall_ptv_70], operator='Subtraction', marginsB = MARGINS.zero)
          site.add_oars(DEF.prostate_bed_nodes_oars + [bladder_ptv, rectum_ptv] + [bowel_ptv, ROIS.bowel_space, wall_ptv_70, wall_ptv_56_temp, wall_ptv_56])
        # Common for all prostate bed (with or without nodes):
        site.add_targets([ROIS.ctv_sb, ctv_70, ptv_70])
      else:
        # Hypofractionated (palliative):
        # Targets:
        ptv = ROI.ROIExpanded(ROIS.ptv_sb.name, ROIS.ptv_sb.type, COLORS.ptv_high, source = ROIS.ctv_sb, margins = MARGINS.prostate_bone_match_expansion)
        site.add_targets([ROIS.ctv_sb, ptv])
        # OARs:
        bladder_ptv = ROI.ROIAlgebra(ROIS.z_bladder.name, ROIS.z_bladder.type, COLORS.bladder, sourcesA = [ROIS.bladder], sourcesB = [ptv], operator='Subtraction', marginsB = MARGINS.uniform_3mm_expansion)
        rectum_ptv = ROI.ROIAlgebra(ROIS.z_rectum.name, ROIS.z_rectum.type, COLORS.rectum, sourcesA = [ROIS.rectum], sourcesB = [ptv], operator='Subtraction', marginsB = MARGINS.uniform_2mm_expansion)
        wall_ptv = ROI.ROIWall(ROIS.z_ptv_wall.name, ROIS.z_ptv_wall.type, COLORS.wall, ptv, 1, 0)
        site.add_oars([bladder_ptv, rectum_ptv, wall_ptv])
    # Create all targets and OARs in RayStation:
    site.create_rois()
