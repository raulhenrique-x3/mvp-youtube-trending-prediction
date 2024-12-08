document.getElementById("prediction-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const form = e.target;
  const data = {
    views: parseInt(form.views.value),
    likes: parseInt(form.likes.value),
    dislikes: parseInt(form.dislikes.value),
    comment_count: parseInt(form.comment_count.value),
  };

  try {
    const response = await fetch("/predict/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();
    document.getElementById("result").innerText = `Result: ${result.result}`;
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("result").innerText = "An error occurred.";
  }
});
