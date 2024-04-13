import psycopg2
from psycopg2 import sql
import datetime

def connect():
    try:
        conn = psycopg2.connect(
            dbname="myGym",
            user="postgres",
            password="7685",
            host="localhost",
            port="5432"
        )
        print("Connection to database successful")
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None







def userRegistration():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    time = int(input("Enter your fitness goal time: "))
    weight = int(input("Enter your fitness goal weight: "))
    fitnessaccomplishments = input("Enter your fitness accomplishments: ")
    healthstats = input("Enter your health stats: ")
    exerciseroutine = input("Enter your exercise routine: ")
    fatpercentage = float(input("Enter your fat percentage: "))
    bonedensity = float(input("Enter your bone density: "))
    schedule = input("Enter your schedule: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Member (name, password, phone, email, time, weight, fitnessaccomplishments, healthstats, exerciseroutine, fatpercentage, bonedensity, schedule) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (name, password, phone, email, time, weight, fitnessaccomplishments, healthstats, exerciseroutine, fatpercentage, bonedensity, schedule))
        conn.commit()
        print("Member successfully registered")
        print("You have been charged $50 for your membership")

        cursor.execute("SELECT registrationid FROM Member ORDER BY registrationid DESC LIMIT 1")
        member_id = cursor.fetchone()[0]

        cursor.execute("INSERT INTO Payments (MemberID, Amount, Service, Status) VALUES (%s, %s, %s, %s)",
                       (member_id, 50.00, 'Membership Fee', 'Unprocessed'))
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()








def removeUser():
    print("Enter the following details to remove a user:")
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Member WHERE phone = %s AND password = %s", (phone, password))
        user = cursor.fetchone()
        
        if user:
            registration_id = user[0]
            
            cursor.execute("DELETE FROM Payments WHERE MemberID = %s", (registration_id,))
            conn.commit()
            
            cursor.execute("DELETE FROM Member WHERE phone = %s AND password = %s", (phone, password))
            conn.commit()
            print("User successfully removed")
        else:
            print("User not found or invalid credentials")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()



def updateUser():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Member WHERE name = %s AND password = %s", (name, password))
        user = cursor.fetchone()
        if user:
            print("Enter new information (leave blank to keep current):")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_time = input("Enter new fitness goal time: ")
            new_weight = input("Enter new fitness goal weight: ")
            new_fitnessaccomplishments = input("Enter new fitness accomplishments: ")
            new_healthstats = input("Enter new health stats: ")
            new_exerciseroutine = input("Enter new exercise routine: ")
            new_fatpercentage = input("Enter new fat percentage: ")
            new_bonedensity = input("Enter new bone density: ")
            new_schedule = input("Enter new schedule: ")

            update_query = "UPDATE Member SET"
            update_params = []

            if new_phone:
                update_query += " phone = %s,"
                update_params.append(new_phone)
            if new_email:
                update_query += " email = %s,"
                update_params.append(new_email)
            if new_time:
                update_query += " time = %s,"
                update_params.append(new_time)
            if new_weight:
                update_query += " weight = %s,"
                update_params.append(new_weight)
            if new_fitnessaccomplishments:
                update_query += " fitnessaccomplishments = %s,"
                update_params.append(new_fitnessaccomplishments)
            if new_healthstats:
                update_query += " healthstats = %s,"
                update_params.append(new_healthstats)
            if new_exerciseroutine:
                update_query += " exerciseroutine = %s,"
                update_params.append(new_exerciseroutine)
            if new_fatpercentage:
                update_query += " fatpercentage = %s,"
                update_params.append(new_fatpercentage)
            if new_bonedensity:
                update_query += " bonedensity = %s,"
                update_params.append(new_bonedensity)
            if new_schedule:
                update_query += " schedule = %s,"
                update_params.append(new_schedule)

            update_query = update_query.rstrip(",") + " WHERE name = %s AND password = %s"
            update_params.extend([name, password])
            cursor.execute(update_query, update_params)
            conn.commit()
            print("User information successfully updated")
        else:
            print("User not found or invalid credentials")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def displayDashboard():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT fitnessaccomplishments, healthstats, exerciseroutine FROM Member WHERE name = %s AND password = %s", (name, password))
        user = cursor.fetchone()
        if user:
            print()
            print()
            print("Your dashboard: ")
            print("Fitness Accomplishments:", user[0])
            print("Health Stats:", user[1])
            print("Exercise Routine:", user[2])
            print()
            print()
            print()
        else:
            print("User not found or invalid credentials")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()



def addTrainer():
    name = input("Enter trainer's name: ")
    email = input("Enter trainer's email: ")
    trainingdayavailable = input("Enter which day you are available for private training sessions: ")
    start_time = input("Enter your starting availability (Time): ")
    end_time = input("Enter your ending availability (Time): ")
    password = input("Enter trainer's password: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Trainer (name, email, trainingdayavailable, start_time, end_time, password) VALUES (%s, %s, %s, %s, %s, %s)",
                       (name, email, trainingdayavailable, start_time, end_time, password))
        conn.commit()
        print("Trainer successfully added to the database")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()





def scheduleClass():
    reg_id = input("Enter your registration ID: ")
    day = input("Enter the desired day for the class: ")
    start_time = input("Enter start time for the session(military time): ")
    end_time = input("Enter end time for the session (in military time): ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Trainer WHERE trainingDayAvailable = %s AND start_time <= %s AND end_time >= %s",
                       (day, start_time, end_time))
        matching_trainers = cursor.fetchall()

        if matching_trainers:
            print("Trainers available on {} between {} and {}:".format(day, start_time, end_time))
            for trainer in matching_trainers:
                print("Trainer ID: {}, Name: {}, Email: {}".format(trainer[0], trainer[1], trainer[2]))

            book_class = input("Do you want to book a class with any of these trainers? (yes/no): ")
            if book_class.lower() == "yes":
                trainerid = input("Enter the Trainer ID you want to book a class with: ")

                valid_trainerids = [str(trainer[0]) for trainer in matching_trainers]
                if trainerid in valid_trainerids:
                    cursor.execute("INSERT INTO Trains (registrationid, trainerid, day, time, duration) VALUES (%s, %s, %s, %s, %s)",
                                   (reg_id, trainerid, day, start_time, str(int(end_time[:2]) - int(start_time[:2])) + ":00"))
                    conn.commit()
                    print("Class successfully booked!")

                    cursor.execute("INSERT INTO Payments (MemberID, Amount, Service, Status) VALUES (%s, %s, %s, %s)",
                                   (reg_id, 10.00, 'Personal Training Session', 'Unprocessed'))
                    conn.commit()
                    print("You have been charged $10 for this class and your payment has been processed.")
                else:
                    print("Invalid Trainer ID.")
            else:
                print("No class booked.")
        else:
            print("No trainer available during the specified time slot")

    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()







def rescheduleClass():
    registration_id = input("Enter your registration ID: ")
    old_day = input("Enter the old day for the class: ")
    old_start_time = input("Enter the old start time for the session (in military time): ")
    old_end_time = input("Enter the old end time for the session (in military time): ")
    new_day = input("Enter the new day for the class: ")
    new_start_time = input("Enter the new start time for the session (in military time): ")
    new_end_time = input("Enter the new end time for the session (in military time): ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Trains WHERE registrationid = %s AND day = %s AND time >= %s AND time <= %s",
                       (registration_id, old_day, old_start_time, old_end_time))
        class_info = cursor.fetchone()

        if class_info:
            new_duration = str(datetime.datetime.strptime(new_end_time, '%H:%M') - datetime.datetime.strptime(new_start_time, '%H:%M'))

            cursor.execute("UPDATE Trains SET day = %s, time = %s, duration = %s WHERE registrationid = %s AND day = %s AND time >= %s AND time <= %s",
                           (new_day, new_start_time, new_duration, registration_id, old_day, old_start_time, old_end_time))
            conn.commit()
            print("Class successfully rescheduled")
        else:
            print("Class with the provided old details not found for the member")

    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()






def cancelClass():
    registration_id = input("Enter your registration ID: ")
    day = input("Enter the day for the class: ")
    start_time = input("Enter the start time for the session (in military time): ")
    end_time = input("Enter the end time for the session (in military time): ")
    confirm = input("Are you sure you want to cancel this class? (yes/no): ")

    if confirm.lower() == "yes":
        conn = connect()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM Trains WHERE registrationid = %s AND day = %s AND time >= %s AND time <= %s",
                           (registration_id, day, start_time, end_time))
            class_info = cursor.fetchone()

            if class_info:
                cursor.execute("DELETE FROM Trains WHERE registrationid = %s AND day = %s AND time >= %s AND time <= %s",
                               (registration_id, day, start_time, end_time))
                conn.commit()
                print("Class successfully canceled")
            else:
                print("Class not found for the provided details")

        except Exception as e:
            print("Error:", e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    else:
        print("Class cancellation canceled")















def viewMemberProfile():
    name = input("Enter the member's name: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT fitnessaccomplishments, healthstats, exerciseroutine FROM Member WHERE name = %s", (name,))
        member_info = cursor.fetchone()

        if member_info:
            print()
            print("Member Profile:")
            print("Fitness Accomplishments:", member_info[0])
            print("Health Stats:", member_info[1])
            print("Exercise Routine:", member_info[2])
            print()
        else:
            print("Member not found")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()






def joinGroupClass():
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Fitness_Classes")
        classes = cursor.fetchall()

        print("Available Group Classes:")
        print("ID\tName\t\tDay\tTime\t\tTrainer ID")
        for group_class in classes:
            print(f"{group_class[0]}\t{group_class[1]}\t\t{group_class[2]}\t{group_class[3]}\t{group_class[4]}")

        join_option = input("Do you want to join any group classes? (yes/no): ")
        if join_option.lower() == "yes":
            class_id = int(input("Enter the ID of the group class you want to join: "))

            registration_id = input("Enter your registration ID: ")

            if any(class_id == group_class[0] for group_class in classes):
                selected_class = next((c for c in classes if c[0] == class_id), None)
                cursor.execute("INSERT INTO Trains (registrationid, trainerid, day, time) VALUES (%s, %s, %s, %s)",
                               (registration_id, selected_class[4], selected_class[2], selected_class[3]))
                conn.commit()
                print("You have successfully joined the group class!")

                cursor.execute("INSERT INTO Payments (MemberID, Amount, Service, Status) VALUES (%s, %s, %s, %s)",
                               (registration_id, 5.00, 'Group Fitness Class', 'Unprocessed'))
                conn.commit()
                print("You have been charged $5 and your payment is in process.")
            else:
                print("Invalid group class ID. Please try again.")

        else:
            print("No group classes joined.")

    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()












def adminServices():
    admin_id = input("Enter your admin ID: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM admin_staff WHERE adminid = %s", (admin_id,))
        admin = cursor.fetchone()

        if admin:
            print("Welcome, {}! What administrative service would you like to access?".format(admin[1]))
            print("1. Add a new fitness class")
            print("2. Book a room for a class")
            print("3. Update a fitness class schedule")
            print("4. Manage Payment")
            print("5. Monitor Fitness Equipment")
            adminChoice = input("Enter your choice: ")

            if adminChoice == "1":
                addFitnessClass()
            elif adminChoice == "2":
                bookRoom()
            elif adminChoice == "3":
                updateClassSchedule()
            elif adminChoice == "4":
                managePayments()
            elif adminChoice  == "5":
                monitorEquipment()
            else:
                print("Invalid choice.")
        else:
            print("Invalid admin ID. Please try again.")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()






def monitorEquipment():
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM fitnessequipment")
        equipment_list = cursor.fetchall()
        print("Fitness Equipment Table:")
        print("ID\tName\t\tLast Maintenance Date\tUpcoming Maintenance Date")
        for equipment in equipment_list:
            print(f"{equipment[0]}\t{equipment[1]}\t{equipment[2]}\t{equipment[3]}")

        equipment_id = int(input("Enter the ID of the equipment you want to update: "))

        update_option = input("Do you want to update lastMaintenanceDate? (yes/no): ")
        if update_option.lower() == "yes":
            new_last_maintenance_date = input("Enter the new lastMaintenanceDate (YYYY-MM-DD): ")
            cursor.execute("UPDATE fitnessEquipment SET lastmaintenancedate = %s WHERE id = %s",
                           (new_last_maintenance_date, equipment_id))
            conn.commit()
            print("lastMaintenanceDate updated successfully.")

        update_option = input("Do you want to update upcomingMaintenanceDate? (yes/no): ")
        if update_option.lower() == "yes":
            new_upcoming_maintenance_date = input("Enter the new upcomingMaintenanceDate (YYYY-MM-DD): ")
            cursor.execute("UPDATE fitnessEquipment SET upcomingmaintenancedate = %s WHERE id = %s",
                           (new_upcoming_maintenance_date, equipment_id))
            conn.commit()
            print("upcomingMaintenanceDate updated successfully.")

    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()




def addFitnessClass():
    name = input("Enter the name of the fitness class: ")
    day = input("Enter the day of the fitness class: ")
    time = input("Enter the time of the fitness class (in military time): ")
    trainer_id = input("Enter the trainer ID for the fitness class: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Fitness_Classes (name, day, time, trainerid) VALUES (%s, %s, %s, %s)",
                       (name, day, time, trainer_id))
        conn.commit()
        print("Fitness class '{}' scheduled for {} at {} with trainer ID {} successfully added.".format(name, day, time, trainer_id))
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()







def bookRoom():
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM room WHERE Availability = True")
        available_rooms = cursor.fetchall()

        print("Available Rooms:")
        print("Room Number\tCapacity\tAvailability\tClass ID\tTime")
        for room in available_rooms:
            print(f"{room[0]}\t\t{room[1]}\t\t{room[2]}\t\t{room[3]}\t\t{room[4]}")

        book_option = input("Do you want to book any of these rooms? (yes/no): ")
        if book_option.lower() == "yes":
            room_number = int(input("Enter the Room Number you want to book: "))

            valid_room_numbers = [room[0] for room in available_rooms]
            if room_number in valid_room_numbers:
                class_id = int(input("Enter the Class ID you want to book: "))
                start_time = input("Enter the start time of the class (in military time): ")

                cursor.execute("UPDATE room SET Time = %s, id = %s, Availability = False WHERE RoomNumber = %s",
                               (start_time, class_id, room_number))
                conn.commit()
                print("Room successfully booked!")
            else:
                print("Invalid room number or room is not available for booking.")

        else:
            print("No room booked.")

    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

















def updateClassSchedule():
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Fitness_Classes")
        classes = cursor.fetchall()

        print("Fitness Classes Table:")
        print("ID\tName\tDay\tTime\tTrainer ID")
        for class_info in classes:
            print(f"{class_info[0]}\t{class_info[1]}\t{class_info[2]}\t{class_info[3]}\t{class_info[4]}")

        class_id = input("Enter the ID of the class you want to update: ")
        new_day = input("Enter new date of class:  ")
        new_time = input("Enter the new time for the class (in military time): ")
        new_trainer_id = input("Enter the new trainer ID for the class: ")

        cursor.execute("SELECT * FROM Fitness_Classes WHERE id = %s", (class_id,))
        class_info = cursor.fetchone()

        if class_info:
            update_query = "UPDATE Fitness_Classes SET"
            update_params = []

            if new_day:
                update_query += " Day = %s,"
                update_params.append(new_day)
            if new_time:
                update_query += " Time = %s,"
                update_params.append(new_time)
            if new_trainer_id:
                update_query += " trainerid = %s,"
                update_params.append(new_trainer_id)

            update_query = update_query.rstrip(",") + " WHERE id = %s"
            update_params.append(class_id)

            cursor.execute(update_query, update_params)
            conn.commit()
            print("Class schedule updated successfully")

        else:
            print("Class not found with the provided ID")

    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()







def managePayments():
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Payments WHERE Status = 'Unprocessed'")
        unprocessed_payments = cursor.fetchall()

        if unprocessed_payments:
            print("Current Payment Table:")
            print("PaymentID\tMemberID\tAmount\tPaymentDate\t\t\tService\t\tStatus")
            for payment in unprocessed_payments:
                print(f"{payment[0]}\t\t{payment[1]}\t\t{payment[2]}\t{payment[3]}\t{payment[4]}\t\t{payment[5]}")

            member_id = input("Enter the ID of the member to process payment: ")
            cursor.execute("UPDATE Payments SET Status = 'Processed' WHERE MemberID = %s AND Status = 'Unprocessed'", (member_id,))
            conn.commit()

            updated_rows = cursor.rowcount
            if updated_rows > 0:
                print(f"Payment for Member ID {member_id} successfully processed.")
            else:
                print("No payments found for the specified member ID.")
        else:
            print("No unprocessed payments found.")

    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()





def main():

    while True:
        print("1. Add a member")
        print("2. Withdraw a member")
        print("3. Update a member's information")
        print("4. View a member's dashboard")
        print("5. Add a Trainer")
        print("6. Schedule a class")
        print("7. Reschedule a class")
        print("8. Cancel a class")
        print("9. View a member's profile")
        print("10. Join a group class")
        print("11. Access Administrative Services")

        choice = input("Enter your choice: ")

        if choice == "1":
            userRegistration()
        elif choice == "2":
            removeUser()
        elif choice == "3":
            updateUser()
        elif choice == "4":
            displayDashboard()
        elif choice == "5":
            addTrainer()
        elif choice == "6":
            scheduleClass()
        elif choice == "7":
            rescheduleClass()
        elif choice == "8":
            cancelClass()
        elif choice == "9":
            viewMemberProfile()
        elif choice=="10":
            joinGroupClass()
        elif choice == "11":
            adminServices()







conn = connect()

main()


