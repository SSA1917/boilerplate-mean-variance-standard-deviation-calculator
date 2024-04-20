import numpy as np

def calculate(parameter_list):

    try: 
        matrix_3x3 = np.reshape(parameter_list, (3,3))

    
        mean_flattened,mean_axis0,mean_axis1  =  np.mean(parameter_list),np.mean(matrix_3x3,axis=0),np.mean(matrix_3x3,axis=1)
        var_flattened,var_axis0,var_axis1  =  np.var(parameter_list),np.var(matrix_3x3,axis=0),np.var(matrix_3x3,axis=1) 
        std_flattened,std_axis0,std_axis1  =  np.std(parameter_list),np.std(matrix_3x3,axis=0),np.std(matrix_3x3,axis=1) 
        max_flattened,max_axis0,max_axis1  =  np.max(parameter_list),np.max(matrix_3x3,axis=0),np.max(matrix_3x3,axis=1)
        min_flattened,min_axis0,min_axis1  =  np.min(parameter_list),np.min(matrix_3x3,axis=0),np.min(matrix_3x3,axis=1) 
        sum_flattened,sum_axis0,sum_axis1  =  np.sum(parameter_list),np.sum(matrix_3x3,axis=0),np.sum(matrix_3x3,axis=1) 

        return {
            'mean': [mean_axis0.tolist(),mean_axis1.tolist(),mean_flattened],
            'variance': [var_axis0.tolist(),var_axis1.tolist(),var_flattened],
            'standard deviation': [std_axis0.tolist(),std_axis1.tolist(),std_flattened],
            'max': [max_axis0.tolist(),max_axis1.tolist(),max_flattened],
            'min': [min_axis0.tolist(),min_axis1.tolist(),min_flattened],
            'sum': [sum_axis0.tolist(),sum_axis1.tolist(),sum_flattened]
        }
    except Exception as error:
        print(type(error).__name__, "List must contain nine numbers")