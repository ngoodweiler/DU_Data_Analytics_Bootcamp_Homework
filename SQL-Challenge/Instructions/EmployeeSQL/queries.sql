-- 01) List employee number, last name, first name, gender, and salary
select e.emp_no, e.last_name, e.first_name, e.gender, s.salary
from employees e
left join salaries s
on e.emp_no = s.emp_no

-- 02) List employees hried in 1986 (emp no, last name, first name, hire date)
select e.emp_no, e.last_name, e.first_name, e.hire_date 
from employees e
where e.hire_date
BETWEEN '1986-01-01' and '1986-12-31';

-- 03) List department managers with dept no, dept name, manager emp no, last name, first name, start and end employment dates
select d.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name, dm.from_date, dm.to_date
from departments d
left join dept_manager dm
on d.dept_no = dm.dept_no
left join employees e
on e.emp_no = dm.emp_no
ORDER BY dept_no ASC, from_date ASC

-- 04) List department of each employee with emp no, last name, first name, department name
select e.emp_no, e.last_name, e.first_name, d.dept_name
from employees e, departments d, dept_emp de
where e.emp_no = de.emp_no and de.dept_no = d.dept_no;

-- 05) List employees with first name Hercules and last name begins with B
select e.emp_no, e.last_name, e.first_name
from employees e
where e.first_name = 'Hercules' and e.last_name like 'B%';

-- 06) List employees in Sale department with emp no, last name, first name, dept name
select e.emp_no, e.last_name, e.first_name, d.dept_name
from employees e, departments d, dept_emp de
where d.dept_name = 'Sales' and 
	e.emp_no = de.emp_no and 
	de.dept_no = d.dept_no
ORDER BY e.emp_no;

-- 07) List employees in Sales and Development depts with emp no, last name, first name, and dept name
select e.emp_no, e.last_name, e.first_name, d.dept_name
from employees e, departments d, dept_emp de
where (d.dept_name = 'Sales' or d.dept_name = 'Development') and 
	e.emp_no = de.emp_no and 
	de.dept_no = d.dept_no
ORDER BY e.emp_no;

-- List frequency count of employee last names in descending order
select e.last_name, count(e.last_name) as number_of_employees
from employees e
GROUP BY e.last_name 
ORDER BY number_of_employees DESC;
