const emp_ids = [
    '002070601',
    '002070606',
    '002102795',
    '002070612',
    '002074979',
    '002070654',
    '002070622',
    '002074987',
    '002072915',
    '002072979',
    '002072961',
    '002074965',
    '002072955',
    '002070598',
    '002070603',
    '002072925',
    '002070548',
    '002070608',
    '002072981',
    '002075006',
    '002070664',
    '002072976',
    '002072919',
    '002094044',
    '002191488',
    '002191486',
    '002209013'
]

const base_url = 'https://example.com/Employee/Profile?employeeId='

for (let i = 0; i < emp_ids.length; i++) {
    await window.open(base_url + emp_ids[i], "_blank")
}