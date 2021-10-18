create table if not exists product (
  product_id bigint generated always as identity primary key,
  name varchar not null,
  price numeric(15, 6) not null,
  shelf_life int not null
);

create table if not exists provider (
  provider_id bigint generated always as identity primary key,
  name varchar not null,
  INN varchar not null,
  bank varchar not null,
  checking_account varchar,
  due_date int
);

create table if not exists batch (
  batch_id bigint generated always as identity primary key,
  date date, 
  count bigint,
  product_id bigint references product(product_id),
  provider_id bigint references provider(provider_id)
);

