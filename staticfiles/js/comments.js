const editButtons = document.querySelectorAll(".btn-edit");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
let commentText = null;

if (commentForm) {
    commentText = commentForm.querySelector('textarea[name="body"]');

    if (commentText && submitButton) {
        editButtons.forEach(button => {
            button.addEventListener("click", (e) => {
                const commentId = button.getAttribute("comment_id");
                const commentContentEl = document.getElementById(`comment${commentId}`);
                if (!commentContentEl) return;

                const commentContent = commentContentEl.innerText.trim();
                commentText.value = commentContent;
                submitButton.innerText = "Update";
                commentForm.setAttribute("action", `edit_comment/${commentId}`);
                commentForm.scrollIntoView({ behavior: "smooth" });
            });
        });
    }
}


const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}
