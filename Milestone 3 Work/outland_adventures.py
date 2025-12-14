import mysql.connector
from mysql.connector import Error
from mysql.connector import MySQLConnection
import dotenv # to use .env file
import os
from dotenv import dotenv_values

# Function that connects to the 'outland_adventures' database and queries related tables

def connect_and_query_outland():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',          # tested with localhost but please change accordingly
            user='root',      
            passwd='password',    # also tested with default password
            database='outland_adventures'
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            cursor = connection.cursor(dictionary=True) 
            
            # Querying essential outland_adventures tables helpful to business decisions

            # --- Querying the 'trip' table ---
            cursor.execute("SELECT * FROM trip")
            trip_records = cursor.fetchall()
            print("\n <<<< Data from 'trip' table >>>> \n")
            for row in trip_records:
                print(row)

            # --- Querying the 'booking' table ---
            cursor.execute("SELECT * FROM booking")
            booking_records = cursor.fetchall()
            print("\n <<<< Data from 'booking' table >>>> \n")
            for row in booking_records:
                print(row)

            # --- Querying the 'equipment' table ---
            cursor.execute("SELECT * FROM equipment")
            equipment_records = cursor.fetchall()
            print("\n <<<< Data from 'equipment' table >>>> \n")
            for row in equipment_records:
                print(row)

                # --- Querying the 'equipmenttransaction' table ---
            cursor.execute("SELECT * FROM equipmenttransaction")
            equipmenttransaction_records = cursor.fetchall()
            print("\n <<<< Data from 'equipmenttransaction' table >>>> \n")
            for row in equipmenttransaction_records:
                print(row)


            # --- Joining Trip and Booking tables for enhanced datasets ---
            join_query = ("SELECT t.tripid, t.destination, t.region, t.startdate, t.enddate, b.tripid, b.bookingdate, b.status, b.numberofparticipants FROM trip t JOIN booking b ON t.tripid = b.tripid")
            cursor.execute(join_query)
            
            joined_records = cursor.fetchall()
            print("\n <<<< Joined Data from 'trip' and 'booking' tables >>>> \n")
            for row in joined_records:
                print(row)


    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("\nMySQL connection is closed")

if __name__ == "__main__":
    connect_and_query_outland()