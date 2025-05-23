const emp_ids = [
    '002070601',
    '002070606',
    '002209013'
]

const base_url = 'https://example.com/Employee/Profile?employeeId='

for (let i = 0; i < emp_ids.length; i++) {
    await window.open(base_url + emp_ids[i], "_blank")
}
