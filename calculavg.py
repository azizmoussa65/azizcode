import csv
import panda
def calculate_average(file_path, column_name):
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            total = 0
            count = 0
            for row in csv_reader:
                if column_name in row:
                    total += float(row[column_name])
                    count += 1
                else:
                    print(f"Column '{column_name}' not found in the CSV file.")
                    return
            
            if count == 0:
                print("No valid entries found in the CSV file.")
                return
            
            average = total / count
            print(f"The average value in column '{column_name}' is {average:.2f}.")
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



#autre fonction



def surface_triangle_base_hauteur(base, hauteur):
  """
  Calcule la surface d'un triangle à l'aide de la base et de la hauteur.

  Args:
    base (float): Longueur de la base du triangle.
    hauteur (float): Longueur de la hauteur du triangle.

  Returns:
    float: Surface du triangle.
  """

  if base <= 0 or hauteur <= 0:
    raise ValueError("La base et la hauteur doivent être positives.")

  surface = (base * hauteur) / 2
  return surface

# Exemple d'utilisation
base = 10.0
hauteur = 8.0

surface = surface_triangle_base_hauteur(base, hauteur)
print(f"La surface du triangle est de {surface:.2f} unités carrées.")
