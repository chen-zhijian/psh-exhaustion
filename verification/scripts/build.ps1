param(
    [switch]$Publish,
    [string]$PdfLatex,
    [string]$IntakeSource,
    [string]$Python = 'python'
)

$ErrorActionPreference = 'Stop'
$buildArguments = @((Join-Path $PSScriptRoot 'build.py'))
if ($Publish) { $buildArguments += '--publish' }
if ($PdfLatex) { $buildArguments += @('--pdflatex', $PdfLatex) }
if ($IntakeSource) { $buildArguments += @('--intake-source', $IntakeSource) }
& $Python @buildArguments
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
