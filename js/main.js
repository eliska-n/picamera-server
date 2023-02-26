async function capture() {
	const url = '/capture'
<<<<<<< HEAD
	try {
		const response = await fetch(url, {
		  method: 'GET',
		});
	  
		if (!response.ok) {
		  throw new Error('Network response was not ok');
		}
	  
		const responseData = await response.json();
	  
		const imageName = responseData.image_name;
	  
		// redirect to the new URL
		window.location.href = `/image/${imageName}`
	  } catch (error) {
		console.error('There was a problem with the fetch operation:', error);
	  };
=======
	fetch(url, {
	  method: 'GET',
	})
	.then(response => {
	  if (!response.ok) {
		throw new Error('Network response was not ok');
	  }
	  return response.json();
	})
	.then(responseData => {
	  // handle the response data here
	  imageName = responseData.image_name
	  window.location.href = `/image/${imageName}`;
	})
	.catch(error => {
	  console.error('There was a problem with the fetch operation:', error);
	});
>>>>>>> 89aa67f2a1a709d49585ba6954a5941d4edaa985
}



