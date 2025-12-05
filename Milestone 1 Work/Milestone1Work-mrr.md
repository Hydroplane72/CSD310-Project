# Matthew Rozendaal
12/4/2025

Milestone 1 work

NOTE: I did use AI to pretty all of this up

 # Business Rules for Case Study
- Permissions (User Roles):
    - Admin
        - JFord
        - BTimmerson
    - Guide
        - JMacnell
        - DMarland
    - Marketing
        - AGallegos
    - Inventory
        - DStravopolous
    - Customer
        - Default User (Customer)
    - Developer
        - MWong

### Functional Requirements  
- **Sales Analysis Module**  
  - Track rental vs. purchase ratios  
  - Generate reports on profitability of equipment sales  

- **Booking Analytics**  
  - Monitor bookings by region (Africa, Asia, Southern Europe)  
  - Identify downward trends in customer interest  

- **Inventory Management System**  
  - Flag items older than 5 years  
  - Track usage, condition, and replacement needs  

- **E-commerce Platform**  
  - Display trip schedules and availability  
  - Enable online equipment rental/purchase  
  - Provide secure payment method  

### Non-Functional Requirements  
- **Scalability:** System must handle growth in customers and trips
- **Reliability:** Accurate reporting and inventory tracking  
- **Security:** Protect customer data and payment information  

 ## Assumptions / Missing Requirements
- Customer demand for guided trips will continue to grow
- A customer may want to book for multiple people at a time
- If the Family member is not of age, then we will want to get a waiver signed
- An ECommerce site will need 2FA abilities
- Customer Account status's will not expand in the future
- FamilyMember Relationship should be a look up table but for simplicity I am not doing that.
- Depending on the language of the Waiver you may not need to know if the child or the parent signed the form. You could technically go off of if the "ParentMemberID" is filled in to know if the waiver is for a child. This would mean SignedByParent and SignedByChild would not be needed.
- Trip.Region should be a look up table
- Booking.Status should be a look up table
- Equipment "Category" and "Condition" should be look up tables
- TwoFactorMethod could be normalized into a look up table, but then in the future if you wanted to add new 2FA something, you would have to add it there.
- Staff.Role should be a look up table and should also stay in parity with Database Roles to keep things as simple as possible.
- There is not a "TripAssignment" table to assign staff to trips. I am assuming that employees will be assigned to all trips anyways and there is no need for a designated "lead".

## Entities & Attributes

**CustomerAccount**
- AccountID (PK)
- AccountName (e.g., "The Smith Family")
- PrimaryContactName
- Email
- Phone
- Username (unique)
- PasswordHash (securely stored, not plain text)
- AccountStatus (Active, Suspended, Closed)
- TwoFactorEnabled (Boolean, default = FALSE)

**FamilyMember**
- MemberID (PK)
- AccountID (FK → CustomerAccount.AccountID)
- Name
- Age
- Relationship (Parent, Child, etc.)

**Trip**
- TripID (PK)
- Destination
- Region (Africa, Asia, Southern Europe)
- StartDate
- EndDate
- Price
- SuggestedMaxParticipants

**Booking**
- BookingID (PK)
- AccountID (FK → CustomerAccount.AccountID)
- TripID (FK → Trip.TripID)
- BookingDate
- Status (Confirmed, Cancelled, Pending)
- NumberOfParticipants

**Equipment**
- EquipmentID (PK)
- Name
- Category (Tent, Backpack, etc.)
- PurchaseDate
- Condition
- AvailableQuantity

**EquipmentTransaction**
- TransactionID (PK)
- AccountID (FK → CustomerAccount.AccountID)
- EquipmentID (FK → Equipment.EquipmentID)
- TransactionType (Rental, Purchase)
- TransactionDate
- Quantity
- MemberID (FK → FamilyMember.MemberID, optional)

**Waiver**
- WaiverID (PK)
- MemberID (FK → FamilyMember.MemberID)
- SignedByMember (Boolean)
- SignedByParent (Boolean)
- ParentMemberID (FK → FamilyMember.MemberID, optional — if under 18)
- DateSigned

**TwoFactorMethod**
- MethodID (PK)
- AccountID (FK → CustomerAccount.AccountID)
- MethodType (SMS, Email, AuthenticatorApp)
- Destination (Phone number, email, or app identifier)
- IsPrimary (Boolean)
- DateEnabled

**Staff**
- StaffID (PK)
- Name
- Role (Guide, Marketing, Inventory, Developer, Admin)
- Responsibilities

---

## Relationships

- **CustomerAccount ↔ FamilyMember**
  - One account can have many family members.
  - Each family member belongs to one account.

- **CustomerAccount ↔ Booking**
  - One account can make many bookings.
  - Each booking belongs to one account.

- **Trip ↔ Booking**
  - One trip can have many bookings.
  - Each booking is for one trip.
  - SuggestedMaxParticipants helps manage capacity.

- **CustomerAccount ↔ EquipmentTransaction**
  - One account can rent or buy multiple equipment items.
  - Each transaction belongs to one account.
  - Optionally linked to a specific family member.

- **FamilyMember ↔ Waiver**
  - Each family member must have a waiver.
  - If under 18, waiver must reference a parent (ParentMemberID).

- **CustomerAccount ↔ TwoFactorMethod**
  - One account can have multiple 2FA methods (e.g., SMS + Authenticator App).
  - TwoFactorEnabled = TRUE if at least one method is active.

- **Equipment ↔ EquipmentTransaction**
  - One equipment item can appear in many transactions.
  - Each transaction involves one equipment item.

- **Staff ↔ Trip**
  - Guides (subset of staff) are assigned to trips.
  - Many-to-many possible.

---


# Diagram Code

Use the below diagram code on this website to be able to easily modify the diagram:

https://dbdiagram.io/d


``` https://dbdiagram.io/d
Table CustomerAccount {
  AccountID int [pk]
  AccountName varchar
  PrimaryContactName varchar
  Email varchar
  Phone varchar
  Username varchar [unique]
  PasswordHash varchar
  AccountStatus varchar
  TwoFactorEnabled boolean
}

Table FamilyMember {
  MemberID int [pk]
  AccountID int [ref: > CustomerAccount.AccountID]
  Name varchar
  Age int
  Relationship varchar
}

Table Waiver {
  WaiverID int [pk]
  MemberID int [ref: > FamilyMember.MemberID]
  SignedByMember boolean
  SignedByParent boolean
  ParentMemberID int [ref: > FamilyMember.MemberID]
  DateSigned date
}

Table Trip {
  TripID int [pk]
  Destination varchar
  Region varchar
  StartDate date
  EndDate date
  Price decimal
  SuggestedMaxParticipants int
}

Table Booking {
  BookingID int [pk]
  AccountID int [ref: > CustomerAccount.AccountID]
  TripID int [ref: > Trip.TripID]
  BookingDate date
  Status varchar
  NumberOfParticipants int
}

Table Equipment {
  EquipmentID int [pk]
  Name varchar
  Category varchar
  PurchaseDate date
  Condition varchar
  AvailableQuantity int
}

Table EquipmentTransaction {
  TransactionID int [pk]
  AccountID int [ref: > CustomerAccount.AccountID]
  EquipmentID int [ref: > Equipment.EquipmentID]
  TransactionType varchar
  TransactionDate date
  Quantity int
  MemberID int [ref: > FamilyMember.MemberID]
}

Table TwoFactorMethod {
  MethodID int [pk]
  AccountID int [ref: > CustomerAccount.AccountID]
  MethodType varchar
  Destination varchar
  IsPrimary boolean
  DateEnabled date
}

Table Staff {
  StaffID int [pk]
  Name varchar
  Role varchar
  Responsibilities text
}

```