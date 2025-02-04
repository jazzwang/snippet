// Instruction:
//
//   Visit https://podcasts.apple.com/us/podcast/id1605906552
//   and paste the following code in Chrome DevTools Console
//

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

lastHeight = 3000
count = 0
scrollHeight = $('div#scrollable-page').scrollHeight
script = ""

async function scrollDown() {
    newHeight = lastHeight + scrollHeight
    $('div#scrollable-page').scroll(0, newHeight)
    console.log("scroll to " + newHeight + ", lastHeight = " + lastHeight + ", count = " + count)
    currentHeight = $('div#scrollable-page').scrollHeight
    if ( currentHeight == lastHeight )
    {
        count++
    } else {
        lastHeight = $('div#scrollable-page').scrollHeight
        count = 0
    }
}

scrollDown()

console.log("title = " + $$('span.episode-details__title-text')[0].textContent)
$$('button.play-button')[0].click()
console.log("url = " + $('audio#apple-music-player').src)
$$('button.play-button')[0].click()