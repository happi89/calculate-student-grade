import { useState } from 'react';

const Form = () => {
	const [name, setName] = useState('');
	const [mark, setMark] = useState(0);
	const [courseCode, setCourseCode] = useState('');

	return (
		<div className='container my-0 mx-auto'>
			<h1 className='text-3xl font-bold text-center my-4'>Grader</h1>
			<form
				className='flex flex-col items-center items-center gap-4'
				onSubmit={(event) => {
					event.preventDefault();
					fetch(
						`https://fastapi-production-92af.up.railway.app/?name=${name}&mark=${mark}&course-code=${courseCode}`,
						{
							method: 'POST',
						}
					)
						.then((response) => response.json())
						.then((json) => alert(json));

					setName('');
					setMark(0);
					setCourseCode('');
				}}>
				<input
					type='text'
					className='bg-gray-300 block rounded-sm p-2'
					placeholder='Name'
					value={name}
					onChange={({ target }) => setName(target.value)}
				/>
				<input
					type='number'
					className='bg-gray-300 block rounded-sm p-2'
					placeholder='Mark'
					value={mark}
					onChange={({ target }) => setMark(target.value)}
				/>
				<input
					type='text'
					className='bg-gray-300 block rounded-sm p-2'
					placeholder='Course Code'
					value={courseCode}
					onChange={({ target }) => setCourseCode(target.value)}
				/>
				<button
					className='text-white bg-blue-500 px-16 py-5 flex items-center justify-center rounded-md shadow-sm h-8'
					type='submit'>
					Calculate
				</button>
			</form>
		</div>
	);
};

export default Form;
