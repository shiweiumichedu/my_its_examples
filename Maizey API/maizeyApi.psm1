function New-MaizeyChat
{
    <#
        .SYNOPSIS
        Creates a new Maizey chat conversation

        .DESCRIPTION
        The New-MaizeyChat function initializes a new chat conversation for a specified Maizey project using the U-M GPT API. It requires a project ID, a prompt, and an API key to authenticate the request.

        .PARAMETER maizeyProjectId
        The unique identifier (GUID) of the Maizey project.

        .PARAMETER prompt
        The initial prompt for the chat conversation.

        .PARAMETER apiKey
        The API key used for authentication with the U-M GPT API.

        .EXAMPLE
        PS C:\> New-MaizeyChat -maizeyProjectId "123e4567-e89b-12d3-a456-426614174000" -prompt "Hello Maizey, why is the sky blue?" -apiKey "your_api_key_here"

        .NOTES
        AUTHOR: kylespl
        LASTEDIT: 12/05/2024 09:00
        VERSION: 1.0
        KEYWORDS: MAIZEY, CHAT, GPT, API, AI
    #>

    [CmdletBinding()]
    param (
        [Parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [guid]$maizeyProjectId,

        [Parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$prompt,

        [Parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$apiKey
    )

    # Set authentication headers
    $apiBase = "https://umgpt.umich.edu/maizey/api" # U-M GPT API gateway URL
    $headers = @{
        Accept = "application/json"
        Authorization = "Bearer $($apiKey)"
        'Content-Type' = "application/json"
    }

    # Generate a new prompt and pull the ID
    $uri = "$($apiBase)/projects/$($maizeyProjectId)/conversation/"
    $newConvo = Invoke-RestMethod -Uri $uri -Headers $headers -Method Post
    $messageId = $newConvo.pk

    # Ask a question
    $query = @{
        'query' = "$($prompt)"
    }
    $uri = "$($apiBase)/projects/$($maizeyProjectId)/conversation/$($messageId)/messages/"
    $newMessage = Invoke-RestMethod -Uri $uri -Headers $headers -Method Post -Body ($query | ConvertTo-Json)
    $maizeyResponse = $newMessage.response

    # Output the response and message ID
    Write-Output $maizeyResponse
    Write-Host "Message ID: $($messageId)" -ForegroundColor Green
}