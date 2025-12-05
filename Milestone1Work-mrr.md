# Matthew Rozendaal
12/4/2025

Milestone 1 work

NOTE: I did us AI to pretty all of this up

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
