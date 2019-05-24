// https://fetch.spec.whatwg.org/#fetch-blob-example
async function ajaxGet(method, params) {
    let input = new URL('/@' + method + '/', document.baseURI); // https://url.spec.whatwg.org/#constructors
    Object.keys(params).forEach(key => input.searchParams.append(key, params[key]));
    // noinspection JSCheckFunctionSignatures
    return (await fetch(input, {method: 'GET'}));
}

// https://stackoverflow.com/a/54620350/8390594
function isValidURL(string) {
    return new RegExp(
        '^(https?:\\/\\/)?' + // protocol
        '((([a-zA-Z\\d]([a-zA-Z\\d-]{0,61}[a-zA-Z\\d])*\\.)+' + // sub-domain + domain name
        '[a-zA-Z]{2,13})' + // extension
        '|((\\d{1,3}\\.){3}\\d{1,3})' + // OR ip (v4) address
        '|localhost)' + // OR localhost
        '(\\:\\d{1,5})?' + // port
        '(\\/[a-zA-Z\\&\\d%_.~+-:@]*)*' + // path
        '(\\?[a-zA-Z\\&\\d%_.,~+-:@=;&]*)?' + // query string
        '(\\#[-a-zA-Z&\\d_]*)?$' // fragment locator
    ).test(string);
}

function copyTextToClipboard(text) {
    // noinspection JSUnresolvedVariable
    if (!navigator.clipboard) {
        let textArea = document.createElement("textarea");
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
            document.execCommand('copy');
        } catch (error) {
            console.error('Fallback: Oops, unable to copy', error);
        }

        document.body.removeChild(textArea);
        return;
    }

    // noinspection JSUnresolvedFunction, JSUnresolvedVariable
    navigator.clipboard.writeText(text).catch(console.error);
}

function addLinks(shortLinks) {
    const linksHolder = document.getElementById('own-links');
    for (let link of shortLinks) {
        let linkFragment = linksHolder.getElementsByTagName('template')[0].content.cloneNode(true);
        linkFragment.querySelector('.link__long-link').textContent = link[0];
        const fullShortUrl = window.location.origin + '/' + link[1];
        linkFragment.querySelector('.link__short-link a').textContent = fullShortUrl;
        linkFragment.querySelector('.link__short-link a').href = link[1];

        linksHolder.prepend(linkFragment);
        linksHolder.firstElementChild.querySelector('.short-link__copy-button').addEventListener('click', function () {
            copyTextToClipboard(fullShortUrl);
        });
    }
}

document.getElementById('shorten-button').addEventListener('click', async () => {
    const url = document.getElementById('shorten-input').value;

    if (isValidURL(url)) {
        addLinks(
            [await (
                await ajaxGet('shorten', {url: url})
            ).json()]
        );
    } else {
        alert("No match");
    }
});

(async () => {
    if (document.USER_ID) {
        addLinks(
            await (
                await ajaxGet('get_user_links', {id: document.USER_ID})
            ).json()
        );
    }
})();
