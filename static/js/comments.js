const editButtons = document.querySelectorAll(".btn-edit");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const commentText = commentForm.querySelector('textarea[name="body"]');

if (commentForm && commentText && submitButton) {
  // Add click event to each edit button
  editButtons.forEach(button => {
    button.addEventListener("click", (e) => {
      const commentId = button.getAttribute("comment_id");
      const commentContentEl = document.getElementById(`comment${commentId}`);

      if (!commentContentEl) return;

      const commentContent = commentContentEl.innerText.trim();

      // Populate the form textarea with the comment's current content
      commentText.value = commentContent;

      // Update submit button text
      submitButton.innerText = "Update";

      // Set the form action dynamically to the edit endpoint
      commentForm.setAttribute("action", `edit_comment/${commentId}`);

      // Scroll to the form for user convenience
      commentForm.scrollIntoView({ behavior: "smooth" });
    });
  });
}
