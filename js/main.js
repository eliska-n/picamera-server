async function capture() {
	const url = '/capture'
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
}



