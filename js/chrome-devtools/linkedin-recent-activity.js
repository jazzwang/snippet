// 1. Open https://www.linkedin.com/in/jazzwang/recent-activity/reactions/
// 2. paste this snippet into Chrome Developer Tool Console

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

for ( let i = 1; i < 100; i++ ) {
    await sleep(1000); // sleep 1 second
    window.scrollTo(0, document.body.scrollHeight);
    console.log(`Iteration: ${i}, Remaining: ${99 - i}`);
}

// find $$("button.see-more") and click each element
/**
 * Selects all buttons with the class 'see-more' using the Console Utilities API
 * and triggers a click event on each element.
 */
try {
  const buttons = $$('button.see-more');

  if (buttons.length > 0) {
    buttons.forEach((button, index) => {
      try {
        button.click();
      } catch (clickError) {
        console.error(`Failed to click button at index ${index}:`, clickError);
      }
    });
    console.log(`Successfully clicked ${buttons.length} button(s).`);
  } else {
    console.warn("No buttons matching 'button.see-more' were found on the page.");
  }
} catch (error) {
  console.error("An error occurred while attempting to find or click buttons:", error);
}