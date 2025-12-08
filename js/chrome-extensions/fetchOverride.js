(() => {
	const { fetch: originalFetch } = window;

	window.fetch = async (...args) => {
		let [resource, config] = args;
		const response = await originalFetch(resource, config);

		const clone = response.clone();
		if (resource.includes('select=media%2Ftranscripts')) {
			clone.json()
				.then(data => {
					if (data && data.media && data.media.transcripts && data.media.transcripts.length > 0) {
						const temporaryDownloadUrl = data.media.transcripts[0].temporaryDownloadUrl;
						console.log("[!NOTE!] Temporary WebVTT Download URL:", temporaryDownloadUrl);
						var dl = document.createElement('a');
						dl.href = temporaryDownloadUrl;
						console.log(dl);
						dl.click();
					} else {
						console.warn("Could not find temporaryDownloadUrl in transcripts data.");
					}
				})
				.catch(err => console.error("Error processing transcripts JSON:", err));
		}
		if (resource.includes('streamContent')) {
			clone.json()
				.then((data) => {
					const hiddenDiv = document.createElement('div')
					hiddenDiv.style.display = 'none';
					hiddenDiv.id = 'transcript-extractor-for-microsoft-stream-hidden-div-with-transcript';
					hiddenDiv.innerHTML = data.entries
						.map(x => x.text)
						.reduce((sum, x) => sum + x, "\n");

					window.document.body.appendChild(hiddenDiv);
				})
				.catch((err) => console.error(err));
		}

		return response;
	};
})();
