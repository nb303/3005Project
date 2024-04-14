CREATE TABLE IF NOT EXISTS public.admin_staff
(
    adminid SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    duty TEXT 
);
CREATE TABLE IF NOT EXISTS public.trainer
(
    trainerid serial PRIMARY KEY,
    name character varying(255) NOT NULL,
    email character varying(255),
    password character varying(255),
    start_time time,
    end_time time,
    trainingdayavailable character varying(20)
);

CREATE TABLE IF NOT EXISTS public.fitness_classes
(
    id serial PRIMARY KEY,
    name character varying(255) NOT NULL,
    day character varying,
    "time" time without time zone,
    trainerid integer,
    CONSTRAINT uq_fitnessclassesname UNIQUE (name),
    CONSTRAINT fk_trainerid FOREIGN KEY (trainerid)
        REFERENCES public.trainer (trainerid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS public.fitnessequipment
(
    id serial PRIMARY KEY,
    name character varying(255),
    lastmaintenancedate date,
    upcomingmaintenancedate date
);


CREATE TABLE IF NOT EXISTS public.member
(
    registrationid serial PRIMARY KEY,
    name character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    phone character varying(20) NOT NULL,
    email character varying(255) NOT NULL,
    "time" integer,
    weight numeric(10,2),
    fitnessaccomplishments text,
    healthstats text,
    exerciseroutine text,
    fatpercentage numeric(10,2),
    bonedensity numeric(10,2),
    schedule text,
    CONSTRAINT member_email_key UNIQUE (email),
    CONSTRAINT member_phone_key UNIQUE (phone),
    CONSTRAINT checktimeandweight CHECK ("time" >= 0 AND weight >= 0)
);


CREATE TABLE IF NOT EXISTS public.room
(
    roomnumber serial PRIMARY KEY,
    capacity integer,
    availability boolean,
    id integer,
    "time" time
);

















CREATE TABLE IF NOT EXISTS public.payments
(
    paymentid SERIAL PRIMARY KEY,
    memberid integer,
    amount numeric(10,2) DEFAULT 75.00,
    paymentdate timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    service character varying(255) COLLATE pg_catalog."default",
    status character varying(255) COLLATE pg_catalog."default" DEFAULT 'Unprocessed'::character varying,
    CONSTRAINT payments_memberid_fkey FOREIGN KEY (memberid)
        REFERENCES public.member (registrationid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT payments_service_check CHECK (service::text = ANY (ARRAY['Membership Fee'::character varying, 'Personal Training Session'::character varying, 'Group Fitness Class'::character varying]::text[]))
);

CREATE TABLE IF NOT EXISTS public.trains
(
    trainid SERIAL PRIMARY KEY,
    registrationid integer,
    trainerid integer,
    day character varying COLLATE pg_catalog."default",
    "time" time without time zone,
    duration interval,
    CONSTRAINT fk_registrationid FOREIGN KEY (registrationid)
        REFERENCES public.member (registrationid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_trainerid FOREIGN KEY (trainerid)
        REFERENCES public.trainer (trainerid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
