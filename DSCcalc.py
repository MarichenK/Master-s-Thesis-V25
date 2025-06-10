from connect import *

patient = get_current("Patient")
case_name = 'caseName'
case = next((c for c in patient.Cases if c.CaseName == case_name), None)
roi_pairs = [['ROI1','ROI2']]
                
data_out = {}
metrics = ['DiceSimilarityCoefficient','MeanDistanceToAgreement','MaxDistanceToAgreement']
for rois in roi_pairs:
    roi_a, roi_b = rois
    dict_val = case.PatientModel.StructureSets["MR 2"].ComparisonOfRoiGeometries(RoiA=roi_a,RoiB=roi_b,ComputeDistanceToAgreementMeasures=True)
    data_out[roi_a] = {metric: str(dict_val[metric]) for metric in metrics}
print("ROI_Name,", ",".join(metrics))
for roi, metrics_dict in data_out.items():
    print(f"{roi}, {', '.join(metrics_dict.values())}")