

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
  LeadGuide int [ref: > Staff.StaffID]
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