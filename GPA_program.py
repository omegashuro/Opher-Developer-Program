def calculate_cumulative_pass_score(credit_value, final_mark, total_credit_value):
  """
    Calculates the cumulative pass score (percentage pass mark) for a student.
    
    Parameters:
    credit_values (list): A list of integers representing the credit value for each module.
    final_marks (list): A list of integers representing the final mark for each module.
    
    Returns:
    float: The cumulative pass score.
    """
  cumulative_pass_score = (sum(credit_value[i] * final_mark[i] for i in range(len(credit_value))) / total_credit_value) * 100
  return cumulative_pass_score



def calculate_gpa(cumulative_pass_score):
  """
    Converts the cumulative pass score to a GPA score.
    
    Parameters:
    cumulative_pass_score (float): The cumulative pass score.
    
    Returns:
    float: The corresponding GPA score.
    """
  if cumulative_pass_score >= 80:
    return 4.0
  elif cumulative_pass_score >= 60:
    return 3.0
  elif cumulative_pass_score >= 50:
    return 2.0
  elif cumulative_pass_score >= 40:
    return 1.0
  else:
    return 0.0

  
 
def determine_eligibility(gpa, department):
   """
    Finds if a student is eligible for enrolment at Yale University and in which department.
    
    Parameters:
    gpa (float): The GPA score of a student.
    departments (list): A list of dictionaries, each representing a department with its minimum GPA requirement.
    
    Returns:
    tuple: A tuple containing a boolean value indicating eligibility and a string representing the eligible department or a message indicating ineligibility.
    """
    
  if department == "Science" and gpa >= 2.8:
    return "Eligible for Science faculty"
  elif department == "Arts" and gpa >= 2.5:
    return "Eligible for Arts department"
  elif department == "Actuarial science":
    if gpa >= 3.5 and gpa <= 4.0:
      return "Eligible for Actuarial science department"
    elif gpa >= 2.9:
      return "Eligible for Actuarial science department with strong pass in Mathematics and Physics"
    else:
      return "Not eligible for Actuarial science department"
  elif department == "Economics":
    if gpa >= 2.0 and gpa <= 3.0:
      return "Eligible for Economics department with strong credit or distinction in Mathematics"
    else:
      return "Not eligible for Economics department"
  else:
    return "Not eligible"

  
  
  
  
  
  
  
  
  
def main(credit_value, final_mark, department):
  total_credit_value = sum(credit_value)
  cumulative_pass_score = calculate_cumulative_pass_score(credit_value, final_mark, total_credit_value)
  gpa = calculate_gpa(cumulative_pass_score)
  eligibility = determine_eligibility(gpa, department)
  return eligibility

# Example usage:
credit_value = [120, 120, 130, 110, 90, 120]
final_mark = [60, 74, 54, 80, 62, 45]
department = "Science"
print(main(credit_value, final_mark, department))

credit_value = [120, 120, 130, 110, 90, 120]
final_mark = [78, 54, 84, 70, 72, 60]
department = "Arts"
print(main(credit_value, final_mark, department))

credit_value = [120, 120, 130, 110, 90, 120]
final_mark = [66, 54, 50, 60, 70, 49]
department = "Actuarial science"
print(main(credit_value, final_mark, department))
