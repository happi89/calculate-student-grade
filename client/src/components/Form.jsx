import { useState } from 'react';

const Form = () => {
	const [name, setName] = useState('');
	const [mark, setMark] = useState('');
	const [courseCode, setCourseCode] = useState('');
	const [result, setResult] = useState('');

	console.log(result);

	return (
		<div className='container my-0 mx-auto'>
			<h1 className='text-3xl font-bold text-center my-4'>Grader</h1>
			<form
				className='flex flex-col items-center items-center gap-4'
				onSubmit={(event) => {
					event.preventDefault();
					if (name && mark && courseCode && mark < 101 && mark >= 0) {
						fetch(
							`https://fastapi-production-7bd2.up.railway.app/?name=${name}&mark=${Number(
								mark
							)}&code=${courseCode}`,
							{
								method: 'POST',
							}
						)
							.then((response) => response.json())
							.then((json) => {
								setResult([json.result[0], json.result[1], json.result[2]]);
							});
					} else {
						alert('invalid inputs');
					}

					setName('');
					setMark('');
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
			<div className='flex flex-col items-center gap-2 mt-12'>
				{result[1]?.length > 1 && (
					<div className='my-0 mx-auto'>
						<p>name: {result[0]?.name}</p>
						<p>mark: {result[0]?.mark}</p>
						<p>code: {result[0]?.code}</p>
						<p>{result[1] + result[2]}</p>
					</div>
				)}
			</div>
		</div>
	);
};

export default Form;
