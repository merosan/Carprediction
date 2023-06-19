<script>
 	import axios from "axios";

	let base_url = 'http://127.0.0.1:5000'
	//let base_url = 'http://merosan.pythonanywhere.com'

	let hour;
	let temperature;
	let weekday = [
		{id:0, name:'Sunday' },
		{id:1, name:'Monday' },
		{id:2, name:'Tuesday' },
		{id:3, name:'Wednesday' },
		{id:4, name:'Thursday' },
		{id:5, name:'Friday' },
		{id:6, name:'Saturday' }
	];
	let richtung = [
		{id:0, name:'Auswärts'},
		{id:1, name:'Einwärts'}
	];

	let fahrzeuge = '...'
	let selected_w;
	let selected_r;
	function handleSubmit() {
		let url =
            base_url +
            "/api/predict?hour=" +
            hour +
            "&temperature=" +
            temperature +
            "&weekday=" +
            selected_w.id +
			"&richtung=" +
			selected_r.id; 

        console.log(url);
        axios.get(url).then((response) => {
            fahrzeuge = response.data.toFixed(0);;
        });
	}
</script>

  
<div class="d-flex align-items-center justify-content-center vh-100">
<div class="container text-center">

	<h1>How many cars can you expect in Zurich {fahrzeuge}</h1>

	<div class="row justify-content-md-center">

		<div class="col col-lg-2">
		  <label for="hour-input">Hour</label>
		  <input type="number" class="form-control" placeholder="Hour" aria-label="Hour" bind:value={hour}>
		</div>

		<div class="col col-lg-2">
		  <label for="temperature-input">Temperature</label>
		  <input type="number" class="form-control" placeholder="Temperature in °C" aria-label="Temperature" bind:value={temperature}>
		</div>
  
		<div class="col col-lg-2">
		  <label for="weekday-input">Weekday</label>
		  <select bind:value={selected_w}>
			  {#each weekday as w}
				  <option value={w}>
					  {w.name}
				  </option>
			  {/each}
		  </select>
		  
		</div>
		<div class="col col-lg-2">
		  <label for="richtung-input">Richtung</label>
		  <select bind:value={selected_r}>
			  {#each richtung as r}
				  <option value={r}>
					  {r.name}
				  </option>
			  {/each}
		  </select>
		  
		</div>
		<div class="col-md-auto">
		  <button type="button" class="btn btn-primary" on:click={handleSubmit}>estimate cars</button>
		</div>
	  </div>
	</div>
	  


</div>