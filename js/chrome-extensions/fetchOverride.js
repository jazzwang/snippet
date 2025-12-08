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
						console.log("[!NOTE!] Temporary WebVTT Download URL:", temporaryDownloadUrl + '?format=json');
						var dl = document.createElement('a');
						dl.href = temporaryDownloadUrl + '?format=json';
						filename = document.querySelector("[data-unique-id='DocumentTitleContent']").innerText + '.json';
						dl.download = filename;
						console.log(dl);
						dl.click();
					}
				})
				.catch(err => console.error("Error processing transcripts JSON:", err));
		}
		return response;
	};
})();
