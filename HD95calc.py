from connect import *
import numpy as np

patient = get_current('Patient')
case_name = 'caseName'
case = next((c for c in patient.Cases if c.CaseName == case_name), None)
structure_set = case.PatientModel.StructureSets["MR 2"]
roi_1_name = 'ROI1'
roi_2_name = 'ROI2'

roi_1 = structure_set.RoiGeometries[roi_1_name]
roi_2 = structure_set.RoiGeometries[roi_2_name]
def get_roi_contour_points(roi):
    contours = []
    for slice in roi.PrimaryShape.Contours:
        for point in slice:
            contours.append([point.x, point.y, point.z])
    return np.array(contours)

contours_1 = get_roi_contour_points(roi_1)
contours_2 = get_roi_contour_points(roi_2)

if len(contours_1) == 0 or len(contours_2) == 0:
    print('En eller begge ROI-ene har ingen konturpunkter')
else:
    def compute_pairwise_dist(points_A, points_B):
        distances = []
        for a in points_A:
            min_dist = np.min(np.linalg.norm(points_B - a, axis = 1))
            distances.append(min_dist)
        return np.array(distances)
    
    dist_1_to_2 = compute_pairwise_dist(contours_1, contours_2)
    dist_2_to_1 = compute_pairwise_dist(contours_2, contours_1)

    hd95 = np.percentile(np.hstack([dist_1_to_2, dist_2_to_1]), 95)

    print(f"95%-Housdorff Distance: {hd95:.2f} cm") 