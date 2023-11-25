import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

def plot_missing_values_heatmap(data):
    """
    Generate a heatmap to visualize missing values in a DataFrame.

    Parameters:
        data (pd.DataFrame): The DataFrame containing your data.

    Returns:
        None (displays the heatmap).
    """
    plt.figure(figsize=(15, 6))
    sns.heatmap(data.isnull(), cmap='viridis', cbar=False, yticklabels=False)
    plt.title('Missing Values Heatmap')
    plt.show()
    
    

def plot_roc_curve(y_true, y_probs_list, labels):
    plt.figure(figsize=(8, 6))
    
    for i in range(len(y_probs_list)):
        fpr, tpr, _ = roc_curve(y_true, y_probs_list[i][:, 1], pos_label=1)
        plt.plot(fpr, tpr, linestyle='--', label=labels[i])
    
    random_probs = [0 for i in range(len(y_true))]
    p_fpr, p_tpr, _ = roc_curve(y_true, random_probs, pos_label=1)
    plt.plot(p_fpr, p_tpr, linestyle='--', color='blue')
    
    plt.title('ROC curve')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='best')
    
    plt.show()