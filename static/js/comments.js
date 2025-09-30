const editButtons = document.querySelectorAll(".btn-edit");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const commentText = commentForm.querySelector('textarea[name="body"]');

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

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


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
}